import telebot
import os
from celery import shared_task
from datetime import datetime, timedelta
from tracker.models import Habit

API_KEY = os.getenv('TELEGRAM_TOKEN')


@shared_task
def reminder_habits():
    now = datetime.now()
    bot = telebot.TeleBot(API_KEY)
    habits = Habit.objects.filter(time__lte=now)

    for habit in habits:
        chat_id = habit.user.telegram_id
        message = f'В {habit.time.strftime("%H:%M")} сделать {habit.action} в {habit.place}'

        try:
            response = bot.send_message(chat_id=chat_id, text=message)

            for i in range(7):
                day = i + 1
                if habit.periodisity == day:
                    habit.time += timedelta(days=day)
                    break

        except Exception as e:
            print(e)

        finally:
            habit.save()
