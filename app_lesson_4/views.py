# -*- coding: cp1251 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('������� �� 4 �������')


# Create your views here.
