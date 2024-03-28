from tracker.apps import TrackerConfig
from django.urls import path
from rest_framework import routers
from tracker.views import HabitViewSet, UserHabitAPIView

app_name = TrackerConfig.name

urlpatterns = [
    path('my_habits/', UserHabitAPIView.as_view(), name='user_habits')
]

router = routers.SimpleRouter()
router.register('habit', HabitViewSet)
urlpatterns += router.urls


# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'habits', HabitViewSet, basename='habit')
