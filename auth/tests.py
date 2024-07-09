from django.contrib.auth.models import User
from django.test import TestCase


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="user1", email="abc@gmail.com", is_staff=True, password="123")
        User.objects.create(username="user2", email="abc2@gmail.com", is_staff=False, password="123")

    def test_blogs(self):
        user_1 = User.objects.get(username="user1")
        user_2 = User.objects.get(username="user2")
        self.assertEqual(user_1.username, 'user1')
        self.assertEqual(user_1.email, 'abc@gmail.com')
        self.assertTrue(user_1.is_staff)

        self.assertEqual(user_2.username, 'user2')
        self.assertEqual(user_2.email, 'abc2@gmail.com')
        self.assertFalse(user_2.is_staff)
