from rest_framework import serializers
from tracker.validators import PleasantHabitValidator
from tracker.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [PleasantHabitValidator(field='related_habit')]
