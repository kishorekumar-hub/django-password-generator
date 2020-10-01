from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random

def home(request):
    return render(request,"generator/home.html",{'password':'dwohdouwh322ui'})

def eggs(request):
    return HttpResponse("<h1>Eggs are Wow!</h1>")

def password(request):
    characters  = list('abcdefghijklmnopqrstuvwxyz')
    thepassword = ''
    length = int(request.GET.get('length',12))
    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request,"generator/password.html",{'password':thepassword})

def about(request):
    return render(request,"generator/about.html")
