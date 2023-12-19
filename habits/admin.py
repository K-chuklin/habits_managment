from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "action",
        "place",
        "time",
        "frequency",
        "award",
        "is_positive",
        "is_public",
        "associated_habit",
        "time_to_complete",
    )
