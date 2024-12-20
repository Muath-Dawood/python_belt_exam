from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.contrib import messages
from .models import Pie

User = get_user_model()

def index(req):
  if req.user.is_authenticated:
    return redirect('/dashboard')
  else:
    return redirect('/accounts/signin')

def dashboard(req):
  pies = Pie.objects.filter(user=req.user)
  return render(req, 'pies/dashboard.html', {'pies': pies})

def list_pies(req):
  pass

def show_pie(req):
  pass

def add_pie(req):
  post_data = {
    'name': req.POST['name'],
    'filling': req.POST['filling'],
    'crust': req.POST['crust']
  }
  user = User.objects.get(id=req.user.id)
  errors = Pie.objects.validate_pie_data(post_data)
  try:
    if len(errors):
      for value in errors.values():
        messages.error(req, value)
      raise ValueError("Messing form fields!")
    new_show = Pie(user=user, **post_data)
    new_show.save()
  except IntegrityError:
    messages.error(req, "Name already exists!")
    return redirect('/dashboard/')
  except ValueError:
    return redirect('/dashboard/')
  else:
    return redirect('/dashboard')


def edit_pie(req, id):
  pass

def delete_pie(req, id):
  pass