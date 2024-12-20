from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

def dashboard(req):
  return render(req, 'pies/dashboard.html')

def list_pies(req):
  pass

def show_pie(req):
  pass

def edit_pie(req, id):
  pass

def delete_pie(req, id):
  pass