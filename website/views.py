from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime

@csrf_exempt
def index(request):
    return render(request, 'index.html', {})

@csrf_exempt
def administrador(request):
    return render(request, 'admin.html', {})
