from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import State
import os

HTML_BEGIN = open(os.path.join(os.path.dirname(__file__),'../templates/HTML_BEGIN.html'), 'r').read()
HTML_END = open(os.path.join(os.path.dirname(__file__),'../templates/HTML_END.html'), 'r').read()

# Build the dictionaries for each handle page

def Homepage(request):
    """
    Renders and returns the homepage for publishing. Uses a dictionary for all
    the variable values marked for django in Homepage.html.
    """

    s = State.objects.get(name="Texas")
    return render(request, 'Homepage.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END, "NAME":s.name})

def About(request):
    """
    Renders and returns the about page for publishing. Uses a dictionary for all
    the variables marked for django in About.html.
    """
    return render(request, 'About.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})

def PageNotFound(request):
    return render(request, 'PageNotFound.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})

def State (request, Pagename):
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
