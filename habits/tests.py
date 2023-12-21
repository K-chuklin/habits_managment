from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit


class HabitTestCase(APITestCase):
    def setUp(self):
        self.habit = Habit.objects.create(place="test_place", action="test_action", is_positive=True)

    def test_habit_create(self):
        data = {
            "place": "test_place_create",
            "action": "test_action_create",
        }

        response = self.client.post(reverse("habits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        data = {
            "place": "test_place_update",
            "action": "test_action_update",
        }

        url = reverse("habits:habit_update", args=[self.habit.pk])
        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_deletion(self):
        url = reverse("habits:habit_delete", args=[self.habit.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_time_to_complete_validation(self):
        data = {
            "place": "test_time_to_complete_validation",
            "action": "do something",
            "time_to_complete": 150,
        }

        response = self.client.post(reverse("habits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {"time_to_complete": ["Время выполнения привычки не должно превышать 120 сек"]})

    def test_freq_validation(self):
        data = {
            "place": "test_frequency_validation",
            "action": "do something",
            "freq": 8,
        }

        response = self.client.post(reverse("habits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {"freq": ["Привычку необходимо выполнять не реже, чем раз в неделю"]})

    def test_associated_habit_validation(self):
        self.habit = Habit.objects.create(place="uuu", action="uuu", is_positive=False)

        data = {"place": "home", "action": "do something", "associated_habit": 2}

        response = self.client.post(reverse("habits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {"associated_habit": ["Связанная привычка должна быть полезной"]})

    def test_is_pl_and_award_or_rel_h_validation(self):
        data = {
            "place": "test_is_pl_and_award_or_rel_h_validation",
            "action": "do something",
            "award": "eat something",
            "is_positive": True,
        }

        response = self.client.post(reverse("habits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {"non_field_errors": ["У приятной привычки не может быть вознаграждения или связанной привычки"]})
