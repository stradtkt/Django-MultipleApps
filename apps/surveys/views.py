# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'surveys/index.html')

def surveys(request):
    return HttpResponse("This is all the surveys")

def new(request):
    return HttpResponse("This is a new survey")
