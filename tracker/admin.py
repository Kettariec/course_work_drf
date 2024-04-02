from django.contrib import admin
from tracker.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('user', 'time', 'action', 'pleasant',
                    'reward', 'complete_time',
                    'place', 'periodicity', 'is_public', 'related_habit',)
