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
    curRHandles = open(os.path.join(os.path.dirname(__file__), '../static/handles/' + curDir + '/' + 'RHandles.txt'), 'r').read()
    curRHashtags = open(os.path.join(os.path.dirname(__file__), '../static/handles/' + curDir + '/' + 'RHashtags.txt'), 'r').read()
    curRClusters = open(os.path.join(os.path.dirname(__file__), '../static/handles/' + curDir + '/' + 'RClusters.txt'), 'r').read()
    curDict["Bio"] = curBio
    curDict["Handle"] = curHandle
    curDict["Name"] = curName
    curDict["Profile"] = curProfile
    curDict["HTML_BEGIN"] = HTML_BEGIN
    curDict["HTML_END"] = HTML_END
    curDict["RHandles"] = curRHandles
    curDict["RHashtags"] = curRHashtags
    curDict["RClusters"] = curRClusters
    MasterHandleDict[curDir] = curDict

MasterHashtagDict = {}
for curDir in HashtagDirs :
    curDict = {}
    curActivity = "hashtags/" + curDir + "/Graphs/" + curDir + "Activity.jpg"
    curRHandles = open(os.path.join(os.path.dirname(__file__), '../static/hashtags/' + curDir + '/' + 'RHandles.txt'), 'r').read()
    curRHashtags = open(os.path.join(os.path.dirname(__file__), '../static/hashtags/' + curDir + '/' + 'RHashtags.txt'), 'r').read()
    curRClusters = open(os.path.join(os.path.dirname(__file__), '../static/hashtags/' + curDir + '/' + 'RClusters.txt'), 'r').read()
    curDesc = open(os.path.join(os.path.dirname(__file__), '../static/hashtags/' + curDir + '/' + 'Description.txt'), 'r').read()
    curDict["Activity"] = curActivity
    curDict["Hashtag"] = curDir
    curDict["Description"] = curDesc
    curDict["HTML_BEGIN"] = HTML_BEGIN
    curDict["HTML_END"] = HTML_END
    curDict["RHandles"] = curRHandles
    curDict["RHashtags"] = curRHashtags
    curDict["RClusters"] = curRClusters
    MasterHashtagDict[curDir] = curDict

MasterClusterDict = {}
for curDir in ClusterDirs :
    curDict = {}
    filePrefix = curDir
    curBio = open(os.path.join(os.path.dirname(__file__), '../static/clusters/' + curDir + '/' + filePrefix + 'Description.txt'), 'r').read()
    curRHandles = open(os.path.join(os.path.dirname(__file__), '../static/clusters/' + curDir + '/' + 'RHandles.txt'), 'r').read()
    curRHashtags = open(os.path.join(os.path.dirname(__file__), '../static/clusters/' + curDir + '/' + 'RHashtags.txt'), 'r').read()
    curRClusters = open(os.path.join(os.path.dirname(__file__), '../static/clusters/' + curDir + '/' + 'RClusters.txt'), 'r').read()
    curDict["Name"] = curDir
    curDict["Description"] = curBio
    curDict["Trend1Pic"] = "clusters/" + curDir + "/Graphs/Trend1.jpg"
    curDict["Trend2Pic"] = "clusters/" + curDir + "/Graphs/Trend2.jpg"
    curDict["HTML_BEGIN"] = HTML_BEGIN
    curDict["HTML_END"] = HTML_END
    curDict["RHandles"] = curRHandles
    curDict["RHashtags"] = curRHashtags
    curDict["RClusters"] = curRClusters
    MasterClusterDict[curDir] = curDict

def Homepage(request):
    """
    Renders and returns the homepage for publishing. Uses a dictionary for all
    the variable values marked for django in Homepage.html.
    """
    return render(request, 'Homepage.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})

def About(request):
    """
    Renders and returns the about page for publishing. Uses a dictionary for all
    the variables marked for django in About.html.
    """
    return render(request, 'About.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})

def PageNotFound(request):
    return render(request, 'PageNotFound.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})

def Handle(request, Pagename):
    """
    Renders and returns the handle page for publishing. Uses a dictionary for all
    the variables marked for django in Handle.html or PageNotFound.html.
    """
    try:
        Dict = MasterHandleDict[Pagename]
    except Exception:
        return render(request, 'PageNotFound.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})
    else :
        return render(request, 'Handle.html', Dict)

def Hashtag(request, Pagename):
    """
    Renders and returns the handle page for publishing. Uses a dictionary for all
    the variables marked for django in PageNotFound.html or Hashtag.html.
    """
    try:
        Dict = MasterHashtagDict[Pagename]
    except Exception:
        return render(request, 'PageNotFound.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})
    else :
        return render(request, 'Hashtag.html', Dict)

def Cluster(request, Pagename):
    """
    Renders and returns the handle page for publishing. Uses a dictionary for all
    the variables marked for django in PageNotFound.html or Cluster.html.
    """
    try:
        Dict = MasterClusterDict[Pagename]
    except Exception:
        return render(request, 'PageNotFound.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})
    else :
        return render(request, 'Cluster.html', Dict)
