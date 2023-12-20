from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    def validate_time_to_complete(self, value):
        if value > 120:
            raise serializers.ValidationError("Время выполнения привычки не должно превышать 120 сек")
        return value

    def validate_freq(self, value):
        if value > 7:
            raise serializers.ValidationError("Привычку необходимо выполнять не реже, чем раз в неделю")
        return value

    def validate_associated_habit(self, value):
        if value and not value.is_positive:
            raise serializers.ValidationError("Связанная привычка должна быть полезной")
        return value

    def validate(self, data):
        associated_habit = data.get("associated_habit")
        award = data.get("award")
        is_positive = data.get("is_positive")

        if associated_habit and award:
            raise serializers.ValidationError("Связанную привычку и вознаграждение нельзя выбирать одновременно")
        elif is_positive and associated_habit or award:
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки"
            )
        return data

    class Meta:
        model = Habit
        fields = "__all__"
