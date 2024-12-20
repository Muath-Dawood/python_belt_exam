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
  if req.user.is_authenticated:
    pies = Pie.objects.filter(user=req.user.id)
    return render(req, 'pies/dashboard.html', {'pies': pies})
  else:
    return redirect('/accounts/signin')

def list_pies(req):
  if req.user.is_authenticated:
    pies = Pie.objects.all()
    return render(req, 'pies/list_pies.html', {'pies': pies})
  else:
    return redirect('/accounts/signin')

def show_pie(req, id):
  if req.user.is_authenticated:
    pie = Pie.objects.get(id=id)
    return render(req, 'pies/show_pie.html', {'pie': pie})
  else:
    return redirect('/accounts/signin')

def add_pie(req):
  if req.user.is_authenticated:
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
  else:
    return redirect('/accounts/signin')

def edit_pie(req, id):
  pie = Pie.objects.get(id=id)
  if req.user.is_authenticated:
    if pie.user.id != req.user.id:
      messages.error(req, "YOU CAN NOT EDIT A PIE THAT IS NOT YOURS!")
      return redirect('/dashboard')
    if req.method == 'GET':
      context = {
      'pie': Pie.objects.get(id=id)
      }
      return render(req, 'pies/edit_pie.html', context)
    if req.method == 'POST':
      post_data = {
        'name': req.POST['name'],
        'filling': req.POST['filling'],
        'crust': req.POST['crust']
      }
      errors = Pie.objects.validate_pie_data(post_data)
      try:
        if len(errors):
          for value in errors.values():
            messages.error(req, value)
          raise ValueError("Messing form fields!")
        for attr in post_data:
          if hasattr(pie, attr):
            setattr(pie, attr, post_data[attr])
        pie.save()
      except IntegrityError:
        messages.error(req, "Name already exists!")
        return redirect('/dashboard/')
      except ValueError:
        return redirect('/dashboard/')
      else:
        return redirect('/dashboard')
  else:
    return redirect('/accounts/signin')

def delete_pie(req, id):
  pie = Pie.objects.get(id=id)
  if req.user.is_authenticated:
    if pie.user.id != req.user.id:
        messages.error(req, "YOU CAN NOT EDIT A PIE THAT IS NOT YOURS!")
        return redirect('/dashboard')
    pie = Pie.objects.get(id=id)
    pie.delete()
  return redirect('/dashboard')