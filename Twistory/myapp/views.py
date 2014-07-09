from django.http import HttpResponse
from django.shortcuts import render

import os

GloablDict = {'Profile' : "Handles/Erik_Spoelstra/ErikSpoelstraProfile.jpg", 'title' : "Erik Spoelstra"}

def homepage(request):
	return render(request, 'Homepage.html', {})

def ErikSpoelstra(request):
    myDict = {"Profile" : "Handles/Erik_Spoelstra/ErikSpoelstraProfile.jpg", "title" : "Erik Spoelstra"}
    return render(request, 'Handle.html', myDict)

def GreggPopovich(request):
    myDict = {"Profile" : "Handles/Gregg_Popovich/GreggPopovichProfile.jpg", "title" : "Gregg Popovich"}
    return render(request, 'Handle.html', myDict)

def LeBronJames(request):
    myDict = {"Profile" : "Handles/LeBron_James/LeBronJamesProfile.jpg", "title" : "LeBron James"}
    return render(request, 'Handle.html', myDict)
