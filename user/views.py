from django.shortcuts import render
from .models import User
import datetime

date = datetime.date.today()

def home(request):
    return render(request, 'user/home.html',{"date": date})

def users(request):
    users = User.objects.all()
    return render(request, 'user/users.html', {"date": date,"users":users})

