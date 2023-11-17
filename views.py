from django.http import HttpResponse
from django.shortcuts import rediect

def index(request):
    return HttpResponse('index')
def login(request):
    return rediect('/index')
