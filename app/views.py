# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello Everyone</h1>')
