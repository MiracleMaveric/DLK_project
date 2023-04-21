from .models import CustomUser
import datetime
from django.test import TestCase


class TestCustomUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create(
            username='root',
            password='root',
            birth_date=datetime.datetime.now(),
        )

    def test_global(self):
        user = CustomUser.objects.get(id=1)
        user.birth_date = datetime.datetime.now() + datetime.timedelta(days=1)
        user.avatar = 'common/img/empty_avatar'
        user.about = str('Hi, it is me, test user') + str('pika-boo')
        user.save()

