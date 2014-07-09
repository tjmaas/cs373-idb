from django.http import HttpResponse
from django.shortcuts import render
import os

# Build the dictionaries for each handle page

HandleDirs = []
for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.path.dirname(__file__),'../static/Handles/')):
    HandleDirs.extend(dirnames)
    break

MasterHandleDict = {}
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
    MasterHandleDict[filePrefix] = curDict

def Homepage(request):
	return render(request, 'Homepage.html')

def Handle(request, Pagename):
    try:
        Dict = MasterHandleDict[Pagename]
    except KeyError:
        return render(request, 'PageNotFound.html', {"Name" : Pagename})
    else :
        return render(request, 'Handle.html', Dict)

def Hashtag(request, Pagename):
    pass

def Cluster(request, Pagename):
    pass