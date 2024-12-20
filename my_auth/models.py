from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model that uses email as the primary identifier
    instead of a username.
    """
    username = None  # Remove the username field
    email = models.EmailField(unique=True)  # Unique email for authentication

    USERNAME_FIELD = 'email'  # Use email to log in
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Required for superuser creation

    def __str__(self):
        return self.email
