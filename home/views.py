"""Imports"""
from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')


def blogList(request):
    return render(request, 'home/blogList.html')
