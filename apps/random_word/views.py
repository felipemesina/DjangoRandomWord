# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(request):
    return render(request, 'random_word/index.html')

def generate(request):
    request.session['number']+= 1
    request.session['random_word'] = get_random_string(length=14)
    return redirect('/')

def reset(request):
    del request.session['number']
    del request.session['random_word']
    return redirect('/')
