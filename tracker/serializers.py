from rest_framework import serializers
from tracker.validators import (RelatedHabitValidator,
                                HabitValidator,
                                HabitPleasantValidator)
from tracker.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [RelatedHabitValidator(field='related_habit'),
                      HabitValidator(field1='related_habit', field2='reward'),
                      HabitPleasantValidator(field1='related_habit',
                                             field2='reward',
                                             field3='pleasant')]
