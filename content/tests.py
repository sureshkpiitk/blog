from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.test import TestCase

from content.models import Blog


class BlogTestCase(TestCase):
    def setUp(self):
        # user create
        User.objects.create(username="user1", email="abc@gmail.com", is_staff=True, password="123")
        User.objects.create(username="user2", email="abc2@gmail.com", is_staff=False, password="123")
        self.user_1 = User.objects.get(username="user1")
        self.user_2 = User.objects.get(username="user2")
        # Blog create
        Blog.objects.create(title="title1", content="some content 1", auther=self.user_1)
        Blog.objects.create(title="title2", content="some content 2", auther=self.user_2)

    def test_blogs(self):
        blog_1 = Blog.objects.get(title="title1")
        blog_2 = Blog.objects.get(title="title2")
        self.assertEqual(blog_1.title, 'title1')
        self.assertEqual(blog_1.content, 'some content 1')
        self.assertEqual(blog_1.auther, self.user_1)
        self.assertEqual(blog_1.created, datetime.now().date())

        self.assertEqual(blog_2.title, 'title2')
        self.assertEqual(blog_2.content, 'some content 2')
        self.assertEqual(blog_2.auther, self.user_2)
        self.assertEqual(blog_2.created, datetime.now().date())


class APIRequestTest(APITestCase):
    def setUp(self):
        User.objects.create(username="user1", email="abc@gmail.com", is_staff=True, password="123")
        User.objects.create(username="user2", email="abc2@gmail.com", is_staff=False, password="123")
        self.user_1 = User.objects.get(username="user1")
        self.user_2 = User.objects.get(username="user2")

    def test_create_blog(self):
        """
        Ensure we can create a new blogs object.
        """
        url = reverse('blog')
        data = {
            "title": "Some blog 1",
            "content": "some content 1",
            "auther": self.user_1.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blog.objects.count(), 1)
        self.assertEqual(Blog.objects.get().title, 'Some blog 1')
        # get blogs
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        updated_data = data
        updated_data["id"] = 1
        updated_data["created"] = str(datetime.now().date())
        self.assertDictEqual(response.data[0], updated_data)

    def test_blogs_with_filter_auther(self):
        url = reverse('blog')
        data = {
            "title": "Some blog 1",
            "content": "some content 1",
            "auther": self.user_1.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blog.objects.count(), 1)
        self.assertEqual(Blog.objects.get().title, 'Some blog 1')
        # filter blogs with auther
        response = self.client.get(url, data={"auther": self.user_1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        updated_data = data
        updated_data["id"] = 1
        updated_data["created"] = str(datetime.now().date())
        self.assertDictEqual(response.data[0], updated_data)

    def test_blog_filter_with_created(self):
        url = reverse('blog')
        data = {
            "title": "Some blog 1",
            "content": "some content 1",
            "auther": self.user_1.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blog.objects.count(), 1)
        self.assertEqual(Blog.objects.get().title, 'Some blog 1')
        # filter blogs with auther
        response = self.client.get(url, data={"created": str(datetime.now().date())})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        updated_data = data
        updated_data["id"] = 1
        updated_data["created"] = str(datetime.now().date())
        self.assertDictEqual(response.data[0], updated_data)

    def test_blog_filter_with_created_and_auther(self):
        url = reverse('blog')
        data = {
            "title": "Some blog 1",
            "content": "some content 1",
            "auther": self.user_1.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blog.objects.count(), 1)
        self.assertEqual(Blog.objects.get().title, 'Some blog 1')
        # filter blogs with auther
        response = self.client.get(url, data={"created": str(datetime.now().date()),
                                              "auther": self.user_1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        updated_data = data
        updated_data["id"] = 1
        updated_data["created"] = str(datetime.now().date())
        self.assertDictEqual(response.data[0], updated_data)

    def test_blog_filter_with_created_and_auther_with_empty_result(self):
        url = reverse('blog')
        data = {
            "title": "Some blog 1",
            "content": "some content 1",
            "auther": self.user_1.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blog.objects.count(), 1)
        self.assertEqual(Blog.objects.get().title, 'Some blog 1')
        # filter blogs with auther
        response = self.client.get(url, data={"created": str(datetime.now().date()),
                                              "auther": self.user_2.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
