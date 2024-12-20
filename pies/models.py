from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Pie(models.Model):
  name = models.CharField(blank=False, unique=True)
  filling = models.CharField(blank=False)
  crust = models.CharField(blank=False)

  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pies')
