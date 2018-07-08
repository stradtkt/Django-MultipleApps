# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def register(request):
    return HttpResponse("This is register")

def login(request):
    return HttpResponse("This is login")

def new(request):
    return HttpResponse("This is a new user")

def users(request):
    return HttpResponse("This is all the users")