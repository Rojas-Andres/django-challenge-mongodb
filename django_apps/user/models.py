"""
Models for core app.
"""

from djongo import models


class User(models.Model):
    """User in the system."""

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=50, blank=True)
    code_phone = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.CharField(max_length=250, blank=True)
    is_anonymous = models.BooleanField(default=True)
    password = models.CharField(max_length=128)
    is_authenticated = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """Return string representation of user."""
        return self.email
