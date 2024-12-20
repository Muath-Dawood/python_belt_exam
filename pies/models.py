from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Pie(models.Model):
  name = models.CharField(blank=False, unique=True, max_length=255)
  filling = models.CharField(blank=False, max_length=255)
  crust = models.CharField(blank=False, max_length=255)

  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pies')
