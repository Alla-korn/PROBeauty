from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.

def get_main_page(request):
    return render(request, 'base.html')
