from django.http import HttpResponse
from django.shortcuts import render
import os

nav_bar = open(os.path.join(os.path.dirname(__file__),'../templates/Navbar.html'), 'r').read()

# Build the dictionaries for each handle page

HandleDirs = []
for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.path.dirname(__file__),'../static/handles/')):
    HandleDirs.extend(dirnames)
    break

HashtagDirs = []
for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.path.dirname(__file__),'../static/hashtags/')):
    HashtagDirs.extend(dirnames)
    break

MasterHandleDict = {}
for curDir in HandleDirs :
    curDict = {}
    filePrefix = curDir.replace("_","")
    curBio = open(os.path.join(os.path.dirname(__file__), '../static/handles/' + curDir + '/' + filePrefix + 'Bio.txt'), 'r').read()
    curHandle = open(os.path.join(os.path.dirname(__file__), '../static/handles/' + curDir + '/' + filePrefix + 'BasicInfo.txt'), 'r').readlines()[1]
    curName = open(os.path.join(os.path.dirname(__file__), '../static/handles/' + curDir + '/' + filePrefix + 'BasicInfo.txt'), 'r').readlines()[0]
    curProfile = "handles/" + curDir + "/" + filePrefix + "Profile.jpg"
    curDict["Bio"] = curBio
    curDict["Handle"] = curHandle
    curDict["Name"] = curName
    curDict["Profile"] = curProfile
    curDict["nav_bar"] = nav_bar
    MasterHandleDict[curDir] = curDict

MasterHashtagDict = {}
for curDir in HashtagDirs :
    curDict = {}
    curActivity = "hashtags/" + curDir + "/Graphs/" + curDir + "Activity.jpg"
    curDict["Activity"] = curActivity
    curDict["Hashtag"] = curDir
    curDict["nav_bar"] = nav_bar
    MasterHashtagDict[curDir] = curDict

def Homepage(request):
	return render(request, 'Homepage.html', {"nav_bar" : nav_bar})

def Handle(request, Pagename):
    try:
        Dict = MasterHandleDict[Pagename]
    except KeyError:
        return render(request, 'PageNotFound.html', {"Name" : Pagename})
    else :
        return render(request, 'Handle.html', Dict)

def Hashtag(request, Pagename):
    try:
        Dict = MasterHashtagDict[Pagename]
    except KeyError:
        return render(request, 'PageNotFound.html', {"Name" : Pagename})
    else :
        return render(request, 'Hashtag.html', Dict)

def Cluster(request, Pagename):
    pass