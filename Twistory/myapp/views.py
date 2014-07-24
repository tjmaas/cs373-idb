from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import State, Park, Hike
import json
import os
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

HTML_BEGIN = open(os.path.join(os.path.dirname(__file__),'../templates/HTML_BEGIN.html'), 'r').read()
HTML_END = open(os.path.join(os.path.dirname(__file__),'../templates/HTML_END.html'), 'r').read()

# Build the dictionaries for each handle page

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





def State_List_API (request):
    List = []

    StateObjects = State.objects.all()

    for obj in StateObjects:
        d = {}
        d["name"] = obj.name
        d["flag"] = obj.flag
        List += d
    return HttpResponse(json.dumps(d),mimetype="application/json")


def State_List (request):
    """
    Renders and returns the handle page for publishing. Uses a dictionary for all
    the variables marked for django in Handle.html or PageNotFound.html.
    """
    HtmlToReturn = ""
    try:
        StateObjects = State.objects.all()
        for obj in StateObjects :
            HtmlToReturn += "<img src=" + obj.flag + ">"
            HtmlToReturn += "<h2><a href=/states/" + obj.name + ">" + obj.name + "</a></h2>"
            HtmlToReturn += "<p></p>"
    except Exception:
        return render(request, 'PageNotFound.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})
    else :
        return render(request, 'StateList.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END, "HTML" : HtmlToReturn})

def State_ID (request, Pagename):
    """
    Renders and returns the handle page for publishing. Uses a dictionary for all
    the variables marked for django in Handle.html or PageNotFound.html.
    """
    try:
        StateObject = State.objects.get(name=Pagename)
        ParksinState = Park.objects.filter(state=StateObject)
        HtmlParks = "<h3>Parks In " + Pagename + "</h3>"
        Dict = {}
        Dict["HTML_BEGIN"] = HTML_BEGIN
        Dict["HTML_END"] = HTML_END
        Dict["name"] = StateObject.name
        Dict["date_founded"] = StateObject.date_founded
        Dict["flag"] = StateObject.flag
        Dict["population"] = locale.format("%d", StateObject.population, grouping=True)
        Dict["size"] = locale.format("%d", StateObject.size, grouping=True)
        Dict["video"] = StateObject.video
        for park in ParksinState :
            newParkName = park.name.replace(" ", "%20")
            HtmlParks += "<li><a href=/parks/" + newParkName + ">" + park.name + "</a></li>"
        Dict["HtmlParks"] = HtmlParks
    except Exception:
        return render(request, 'PageNotFound.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})
    else :
        return render(request, 'State.html', Dict)

def Park_List (request):
    """
    Renders and returns the handle page for publishing. Uses a dictionary for all
    the variables marked for django in Handle.html or PageNotFound.html.
    """
    HtmlToReturn = ""
    try:
        ParkObjects = Park.objects.all()
        for obj in ParkObjects :
            newParkName = obj.name.replace(" ", "%20")
            HtmlToReturn += "<img src=" + obj.park_image + ">"
            HtmlToReturn += "<h2><a href=/parks/" + newParkName + ">" + obj.name + "</a></h2>"
            HtmlToReturn += "<p></p>"
    except Exception:
        return render(request, 'PageNotFound.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})
    else :
        return render(request, 'StateList.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END, "HTML" : HtmlToReturn})


def Park_ID (request, Pagename):
    """
    Renders and returns the handle page for publishing. Uses a dictionary for all
    the variables marked for django in Handle.html or PageNotFound.html.
    """

    try:
        ParkObject = Park.objects.get(name=Pagename)
        Dict = {}
        name = ParkObject.name
        name.replace(" ", "")
        Dict["HTML_BEGIN"] = HTML_BEGIN
        Dict["HTML_END"] = HTML_END
        Dict["state"] = ParkObject.state.name
        Dict["name"] = name
        Dict["size"] = ParkObject.size
        Dict["max_elevation"] = ParkObject.max_elevation
        Dict["date_founded"] = ParkObject.date_founded
        Dict["park_image"] = ParkObject.park_image
        Dict["num_visitors"] = ParkObject.num_visitors
        Dict["video"] = ParkObject.video
    except Exception:
        return render(request, 'PageNotFound.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})
    else :
        return render(request, 'Park.html', Dict)

def Hike_List (request):
    """
    Renders and returns the handle page for publishing. Uses a dictionary for all
    the variables marked for django in Handle.html or PageNotFound.html.
    """
    HtmlToReturn = ""
    try:
        HikeObjects = Hike.objects.all()
        for obj in HikeObjects :
            HtmlToReturn += "<img src=" + obj.hike_image + ">"
            HtmlToReturn += "<h2><a href=/hikes/" + obj.name.replace(" ", "%20") + ">" + obj.name + "</a></h2>"
            HtmlToReturn += "<p></p>"
    except Exception:
        return render(request, 'PageNotFound.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})
    else :
        return render(request, 'HikeList.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END, "HTML" : HtmlToReturn})

def Hike_ID (request, Pagename):
    """
    Renders and returns the handle page for publishing. Uses a dictionary for all
    the variables marked for django in Handle.html or PageNotFound.html.
    """
    try:
        HikeObject = Hike.objects.get(name=Pagename)
        Dict = {}
        Dict["HTML_BEGIN"] = HTML_BEGIN
        Dict["HTML_END"] = HTML_END
        Dict["name"] = HikeObject.name
        Dict["distance"] = HikeObject.distance
        Dict["est_time"] = HikeObject.est_time
        Dict["hike_image"] = HikeObject.hike_image
        Dict["difficulty"] = HikeObject.difficulty
        Dict["park"] = HikeObject.park.name
    except Exception:
        return render(request, 'PageNotFound.html', {"HTML_BEGIN" : HTML_BEGIN, "HTML_END" : HTML_END})
    else :
        return render(request, 'Hike.html', Dict)
