import telebot
import os
from celery import shared_task
from datetime import datetime, timedelta
from tracker.models import Habit
import pytz
from django.conf import settings

API_KEY = os.getenv('TELEGRAM_TOKEN')


@shared_task
def reminder_habits():
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.now(zone)
    bot = telebot.TeleBot(API_KEY)
    habits = Habit.objects.filter(time__lte=now)

    for habit in habits:
        chat_id = habit.user.telegram_id
        message = (f'В {habit.time.strftime("%H:%M")} '
                   f'сделать {habit.action} в {habit.place}')

        try:
            response = bot.send_message(chat_id=chat_id,
                                        text=message)
            habit.time += timedelta(days=habit.periodicity)
            break

        except Exception as e:
            print(e)

        finally:
            habit.save()
