from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PieManager(models.Manager):
  def validate_pie_data(self, post_data):
    errors = {}
    if not post_data['name']:
      errors['no_title'] = "You must fill the Name field!"
    if not post_data['filling']:
      errors['no_network'] = "You must fill the Filling field!"
    if not post_data['release_date']:
      errors['no_release_date'] = "You must fill the Crust field!"
    return errors

class Pie(models.Model):
  name = models.CharField(blank=False, unique=True, max_length=255)
  filling = models.CharField(blank=False, max_length=255)
  crust = models.CharField(blank=False, max_length=255)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pies')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = PieManager()
