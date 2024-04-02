from rest_framework.serializers import ValidationError


class HabitValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)

        if related_habit and reward:
            raise ValidationError('Можно выбрать только '
                                  'связанную привычку или вознаграждение!')


class RelatedHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_value = dict(value).get(self.field)

        if field_value:
            if field_value.pleasant is False:
                raise ValidationError('Связанной может '
                                      'быть только приятная привычка!')


class HabitPleasantValidator:

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)
        pleasant = dict(value).get(self.field3)

        if pleasant and reward or pleasant and related_habit:
            raise ValidationError('У приятной привычки не может быть'
                                  ' вознаграждения или связанной привычки')
