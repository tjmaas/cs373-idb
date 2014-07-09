from django.http import HttpResponse
from django.shortcuts import render
import os

# Get Bios for pages
LeBronJamesBio = open(os.path.join(os.path.dirname(__file__), '../static/Handles/LeBron_James/LeBronJamesBio.txt'), 'r').read()
ChrisBoshBio = open(os.path.join(os.path.dirname(__file__), '../static/Handles/Chris_Bosh/ChrisBoshBio.txt'), 'r').read()
DwyaneWadeBio = open(os.path.join(os.path.dirname(__file__), '../static/Handles/Dwyane_Wade/DwyaneWadeBio.txt'), 'r').read()

def homepage(request):
	return render(request, 'Homepage.html', {})

def ErikSpoelstra(request):
    myDict = {"Profile" : "Handles/Erik_Spoelstra/ErikSpoelstraProfile.jpg", "title" : "Erik Spoelstra"}
    return render(request, 'Handle.html', myDict)

def GreggPopovich(request):
    myDict = {"Profile" : "Handles/Gregg_Popovich/GreggPopovichProfile.jpg", "title" : "Gregg Popovich"}
    return render(request, 'Handle.html', myDict)

def LeBronJames(request):
    myDict = {"Profile" : "Handles/LeBron_James/LeBronJamesProfile.jpg", "title" : "LeBron James", "Bio" : LeBronJamesBio}
    return render(request, 'Handle.html', myDict)

def ChrisBosh(request) :
    myDict = {"Profile" : "Handles/Chris_Bosh/ChrisBoshProfile.jpg", "title" : "Chris Bosh", "Bio" : ChrisBoshBio}
    return render(request, 'Handle.html', myDict)

def DwyaneWade(request) :
    myDict = {"Profile" : "Handles/Dwyane_Wade/DwyaneWadeProfile.jpg", "title" : "Dwyane Wade", "Bio" : DwyaneWadeBio}
    return render(request, 'Handle.html', myDict)