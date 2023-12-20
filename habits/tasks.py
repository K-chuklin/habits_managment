import os
import celery
import datetime
import telebot
from habits.models import Habit


@shared_task
def habit_reminder():
    TG_TOKEN = os.getenv("TG_TOKEN")
    bot = telebot.TeleBot(TG_TOKEN, parse_mode=None)
    today = datetime.date.today()
    data = Habit.objects.all()
    for habit in data:
        if habit.time is None:
            continue
        if habit.time.datetime.date() == today:
            bot.send_message(
                chat_id=habit.user.telegram_id,
                text=f"Время для привычки {habit.action}, \n "
                     f"её следует выполнить в {habit.place} в {habit.time}")
