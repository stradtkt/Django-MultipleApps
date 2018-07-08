# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'blogs/index.html')

def new(request):
    return HttpResponse("This is where a new blog post will be held")

def create(request):
    return HttpResponse("This is where you create a new blog post")

def display(request):
    return HttpResponse("This is the post you want to display")

def edit(request):
    return HttpResponse("This is the post you want to edit")

def delete(request):
    return HttpResponse("This is the post you want to delete")