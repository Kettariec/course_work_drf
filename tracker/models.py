from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             default=1, verbose_name="пользователь", related_name='habit')
    place = models.CharField(verbose_name='место выполнения', max_length=50)
    time = models.DateTimeField(verbose_name='время выполнения')
    action = models.CharField(max_length=150, verbose_name='действие')
    pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL,
                                      **NULLABLE, verbose_name='связанная привычка')
    periodicity = models.PositiveIntegerField(default=1, verbose_name='периодичность(в днях)')
    reward = models.CharField(max_length=150, **NULLABLE, verbose_name='вознаграждение')
    complete_time = models.PositiveIntegerField(verbose_name='время выполнения')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
