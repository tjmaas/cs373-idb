from django.http import HttpResponse
from django.shortcuts import render
import os

HandleDirs = []
for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.path.dirname(__file__),'../static/Handles/')):
    HandleDirs.extend(dirnames)
    break

MasterDict = {}
for curDir in HandleDirs :
    curDict = {}
    filePrefix = curDir.replace("_","")
    curBio = open(os.path.join(os.path.dirname(__file__), '../static/Handles/' + curDir + '/' + filePrefix + 'Bio.txt'), 'r').read()
    curHandle = open(os.path.join(os.path.dirname(__file__), '../static/Handles/' + curDir + '/' + filePrefix + 'BasicInfo.txt'), 'r').readlines()[1]
    curName = open(os.path.join(os.path.dirname(__file__), '../static/Handles/' + curDir + '/' + filePrefix + 'BasicInfo.txt'), 'r').readlines()[0]
    curProfile = "Handles/" + curDir + "/" + filePrefix + "Profile.jpg"
    curDict["Bio"] = curBio
    curDict["Handle"] = curHandle
    curDict["Name"] = curName
    curDict["Profile"] = curProfile
    MasterDict[filePrefix] = curDict

def homepage(request):
	return render(request, 'Homepage.html', {})

def handle(request, PageName):
    return render(request, 'Handle.html', MasterDict[PageName])