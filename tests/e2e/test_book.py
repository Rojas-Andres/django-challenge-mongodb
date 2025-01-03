from django.test import TestCase
from django.urls import reverse
from faker import Faker
from rest_framework.test import APIClient
from django_apps.user.models import User
from django_apps.book.models import Book

fake = Faker()


class CreateBookViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("create_book_view")
        self.user = User.objects.create(
            first_name="felipe",
            last_name="felipe",
            document="333330",
            email="felipe@gmail.com",
            code_phone="57",
            phone_number="4444444",
            password="1234516",
        )
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_book(self):
        response = self.client.post(
            self.url,
            {
                "title": fake.user_name(),
                "author": "Gabrie2l22133",
                "published_date": "2023-04-12",
                "genre": fake.user_name(),
                "price": 1233,
            },
        )
        assert response.data["author"] == "Gabrie2l22133"
        assert response.data["price"] == 1233
