from django.http import HttpResponse
from django.shortcuts import render
import os

HTML_BEGIN = open(os.path.join(os.path.dirname(__file__),'../templates/HTML_BEGIN.html'), 'r').read()
HTML_END = open(os.path.join(os.path.dirname(__file__),'../templates/HTML_END.html'), 'r').read()

# Build the dictionaries for each handle page

HandleDirs = []
for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.path.dirname(__file__),'../static/handles/')):
    HandleDirs.extend(dirnames)
    break

HashtagDirs = []
for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.path.dirname(__file__),'../static/hashtags/')):
    HashtagDirs.extend(dirnames)
    break

ClusterDirs = []
for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.path.dirname(__file__),'../static/clusters/')):
    ClusterDirs.extend(dirnames)
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
    curDict["HTML_BEGIN"] = HTML_BEGIN
    curDict["HTML_END"] = HTML_END
    MasterHandleDict[curDir] = curDict

MasterHashtagDict = {}
for curDir in HashtagDirs :
    curDict = {}
    curActivity = "hashtags/" + curDir + "/Graphs/" + curDir + "Activity.jpg"
    curDict["Activity"] = curActivity
    curDict["Hashtag"] = curDir
    curDict["HTML_BEGIN"] = HTML_BEGIN
    curDict["HTML_END"] = HTML_END
    MasterHashtagDict[curDir] = curDict

MasterClusterDict = {}
for curDir in ClusterDirs :
    curDict = {}
    curDict["HTML_BEGIN"] = HTML_BEGIN
    curDict["HTML_END"] = HTML_END
    MasterClusterDict[curDir] = curDict

def Homepage(request):
	return render(request, 'Homepage.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})

def About(request):
    return render(request, 'About.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})

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
    try:
        Dict = MasterClusterDict[Pagename]
    except KeyError:
        return render(request, 'PageNotFound.html', {"Name" : Pagename})
    else :
        return render(request, 'Cluster.html', Dict)