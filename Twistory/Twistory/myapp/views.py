from django.http import HttpResponse
from django.shortcuts import render

import os

KingJamesBioString = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), '../static/KingJamesBio.txt'), 'r').readlines()[0]

GloablDict = {'Profile' : "/handles/Erik_Spoelstra/ErikSpoelstraProfile.jpg", 'title' : "Erik Spoelstra"}
	
def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request):
	image_data = "ChrisBosh.jpg"
	return render(request, 'current_datetime.html', {'img_addr' : image_data })

def homepage(request):
	return render(request, 'current_datetime.html', GloablDict)

def KingJames(request):
    return render(request, 'KingJames.html', GloablDict)
