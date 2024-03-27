from rest_framework import viewsets
from tracker.serializers import HabitSerializer
from tracker.models import Habit


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
