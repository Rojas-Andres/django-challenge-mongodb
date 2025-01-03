from django.test import TestCase
from django.urls import reverse
from faker import Faker
from rest_framework.test import APIClient
from django_apps.user.models import User

fake = Faker()


class UserCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.url = reverse("user_create")

    def test_create_user(self):
        data = {
            "first_name": fake.user_name(),
            "last_name": fake.user_name(),
            "document": str(fake.random_number()),
            "code_phone": "57",
            "email": fake.email(),
            "phone_number": str(fake.random_number()),
            "password": fake.password(),
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 201)
        self.assertNotIn("password", response.data)


class UserListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            first_name="Andres",
            last_name="Andres",
            document="1554510",
            email="andres@gmail.com",
            code_phone="57",
            phone_number="3000000000",
            password="123456",
        )
        self.user.save()
        self.user2 = User.objects.create(
            first_name="felipe",
            last_name="felipe",
            document="333330",
            email="felipe@gmail.com",
            code_phone="57",
            phone_number="4444444",
            password="1234516",
        )
        self.user2.save()
        self.url = reverse("user_list")

    def test_filter_user_not_found(self):
        response = self.client.get(self.url, {"email": "fake@email.com"})
        assert response.json()["results"] == []

    def test_get_all_users(self):
        response = self.client.get(self.url)
        assert len(response.json()["results"]) > 0

    def test_filter_user_found(self):
        response = self.client.get(self.url, {"email": "andres@gmail.com"})
        assert len(response.json()["results"]) == 1
        assert response.json()["results"][0]["email"] == "andres@gmail.com"
