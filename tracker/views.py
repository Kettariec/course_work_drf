from rest_framework import viewsets, generics
from tracker.serializers import HabitSerializer
from tracker.models import Habit
from tracker.permissions import IsOwner
from tracker.pagination import HabitPagination


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination

    def get_permissions(self):
        """Разрешения для разных типов запроса"""
        if self.action == 'retrieve' or 'update' or 'destroy':
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Присваивание пользователя к привычке"""
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()

    def get_queryset(self):
        """Вывод только опубликованных привычек"""
        queryset = Habit.objects.filter(is_public=True)
        return queryset


class UserHabitAPIView(generics.ListAPIView):
    """Вывод привычек пользователя"""
    serializer_class = HabitSerializer

    def get_queryset(self):
        queryset = Habit.objects.filter(user=self.request.user)
        return queryset
