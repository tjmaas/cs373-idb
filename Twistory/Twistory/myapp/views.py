from django.http import HttpResponse
from django.shortcuts import render

import datetime

def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request):
	now = datetime.datetime.now()
	return render(request, 'current_datetime.html', {'current_date' : now })

def homepage(request):
	image_data = "ChrisBosh.jpg"
	return render(request, 'current_datetime.html', {'img_addr' : image_data })
