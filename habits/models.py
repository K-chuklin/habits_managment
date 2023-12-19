from django.db import models
from users.models import User, NULLABLE


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь", **NULLABLE)
    place = models.CharField(max_length=100, verbose_name="место")
    time = models.DateTimeField(verbose_name="время", **NULLABLE)
    action = models.CharField(max_length=100, verbose_name="действие")
    freq = models.PositiveSmallIntegerField(default=1, verbose_name="периодичность", **NULLABLE)
    award = models.CharField(max_length=150, verbose_name="вознаграждение", **NULLABLE)
    is_positive = models.BooleanField(default=False, verbose_name="положительность привычки", **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name="публичность", **NULLABLE)
    associated_habit = models.ForeignKey("self", verbose_name="связанная привычка",
                                         on_delete=models.CASCADE,
                                         **NULLABLE)
    time_to_complete = models.PositiveIntegerField(default=30, verbose_name="время на выполнение", **NULLABLE)

    def __str__(self):
        return f"{self.action}: {self.place}, {self.time}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"

