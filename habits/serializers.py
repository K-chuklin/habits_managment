from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    def validate_time_of_completation(self, value):
        if value > 120:
            raise serializers.ValidationError("Время выполнения привычки не должно превышать 120 сек.")
        return value

    def validate_frequency(self, value):
        if value > 7:
            raise serializers.ValidationError("Привычку необходимо выполнять нереже, чем раз в неделю.")
        return value

    def validate_associated_habit(self, value):
        if value and not value.is_pleasant:
            raise serializers.ValidationError("Связанная привычка должна быть полезной")
        return value

    def validate(self, data):
        associated_habit = data.get("related_habit")
        award = data.get("award")
        is_positive = data.get("is_pleasant")

        if associated_habit and award:
            raise serializers.ValidationError("Связанную привычку и вознаграждение нельзя выбирать одновременно")
        elif is_positive and associated_habit or award:
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            )
        return data

    class Meta:
        model = Habit
        fields = "__all__"
