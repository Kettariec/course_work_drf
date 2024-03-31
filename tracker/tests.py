from rest_framework.test import APITestCase, APIClient
from users.models import User
from tracker.models import Habit
from rest_framework import status


class HabitTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.org',
                                        password='qwertyui')
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place="test",
            time="2024-03-30 12:00",
            action="test",
            complete_time=2,
            reward='test',
            is_public=True,
        )

    def test_create_habit(self):
        data = {
            "place": 'test',
            "time": "2024-03-30 12:00",
            "action": "test",
            "complete_time": 2,
            "reward": "test",
        }
        response = self.client.post(
            'http://127.0.0.1:8000/tracker/habit/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': 2, 'user': self.user.pk,
             'place': 'test', 'time': '2024-03-30T12:00:00+03:00',
             'action': 'test', 'pleasant': False,
             'related_habit': None, 'periodicity': 1,
             'reward': 'test', 'complete_time': 2, 'is_public': False}
        )

    def test_habit_list(self):
        response = self.client.get(
            'http://127.0.0.1:8000/tracker/habit/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.habit.id,
                        "place": self.habit.place,
                        "time": "2024-03-30T12:00:00+03:00",
                        "action": self.habit.action,
                        "pleasant": self.habit.pleasant,
                        "periodicity": self.habit.periodicity,
                        "reward": self.habit.reward,
                        "complete_time": self.habit.complete_time,
                        "is_public": self.habit.is_public,
                        "user": self.habit.user.pk,
                        "related_habit": self.habit.related_habit
                    }
                ]
            }
        )

    def test_habit_retrieve(self):
        response = self.client.get(
            f'http://127.0.0.1:8000/tracker/habit/{self.habit.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "id": self.habit.id,
                "place": self.habit.place,
                "time": "2024-03-30T12:00:00+03:00",
                "action": self.habit.action,
                "pleasant": self.habit.pleasant,
                "periodicity": self.habit.periodicity,
                "reward": self.habit.reward,
                "complete_time": self.habit.complete_time,
                "is_public": self.habit.is_public,
                "user": self.habit.user.pk,
                "related_habit": self.habit.related_habit,
            }
        )

    def test_update_habit(self):
        data = {
            "place": 'new test place',
        }
        response = self.client.patch(
            f'http://127.0.0.1:8000/tracker/habit/{self.habit.pk}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "id": self.habit.id,
                "place": 'new test place',
                "time": "2024-03-30T12:00:00+03:00",
                "action": self.habit.action,
                "pleasant": self.habit.pleasant,
                "periodicity": self.habit.periodicity,
                "reward": self.habit.reward,
                "complete_time": self.habit.complete_time,
                "is_public": self.habit.is_public,
                "user": self.habit.user.pk,
                "related_habit": self.habit.related_habit,
            }
        )

    def test_delete_habit(self):
        response = self.client.delete(
            f'http://127.0.0.1:8000/tracker/habit/{self.habit.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
