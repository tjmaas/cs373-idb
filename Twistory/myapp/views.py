from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models import State, Park, Hike
import urllib.request
import json
import os
import locale
from haystack.query import SearchQuerySet

# used for getting random background image
import random
import os.path

locale.setlocale(locale.LC_ALL, 'en_US')

HTML_BEGIN = open(os.path.join(os.path.dirname(__file__),'../templates/HTML_BEGIN.html'), 'r').read()

# Build the dictionaries for each page

def Homepage(request):
    """
    Renders and returns the homepage for publishing. Uses a dictionary for all
    the variable values marked for django in Homepage.html.
    """
    return render(request, 'Homepage.html')

def About(request):
    """
    Renders and returns the about page for publishing. Uses a dictionary for all
    the variables marked for django in About.html.
    """
    return render(request, 'About.html')

def PageNotFound(request):
    return render(request, 'PageNotFound.html')


def Hungry(request):
    response = urllib.request.urlopen('https://regionalfoods.pythonanywhere.com/api/recipe/')
    recipes_json = list(eval(response.read().decode("utf-8")))

    HtmlToReturn = "<div class=\"row\">"
    try:
        inRow = 0
        for item in recipes_json:
            d = item["fields"]
            # if (inRow == 3) :
            #     HtmlToReturn += "</div> <div class=\"row\">"
            #     inRow = 0
            """
            HtmlToReturn += "<div class=\"col-lg-4 col-sm-6 col-xs-12\"><img src=\"" + "https://regionalfoods.pythonanywhere.com" + d["image"] + "\" class=\"thumbnail img-responsive\"><div class=\"starter-template\"><h2>" + d["name"] +  "</h2></a></div></div>"
            """
            HtmlToReturn += "<div class=\"modal fade\" id=\"basicModal" + str(item["pk"]) + "\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"" + d["name"] + "\" aria-hidden=\"true\"><div class=\"modal-dialog\"><div class=\"modal-content\"><div class=\"modal-header\"><h4 class=\"modal-title\" id=\"myModalLabel\">Cooking Instructions:</h4></div><div class=\"modal-body\"><h3>" + d["instructions"] + "</h3></div></div></div></div>" + "<div class=\"col-lg-4 col-sm-6 col-xs-12\"><img src=\"" + "https://regionalfoods.pythonanywhere.com" + d["image"] + "\" class=\"thumbnail img-responsive\"><div class=\"homepage\"><h2>" + "<a href=\"#\" class=\"tn btn-lg  btn-info\" data-toggle=\"modal\" data-target=\"#basicModal" + str(item["pk"]) + "\">" + d["name"] + "</a>" + "</h2></a></div></div>"
            #<a href="#" class="btn btn-lg btn-success" data-toggle="modal" data-target="#basicModal">d["name"]</a>
            #"<div class=\"modal fade\" id=\"basicModal\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"basicModal\" aria-hidden=\"true\"><div class=\"modal-dialog\"><div class=\"modal-content\"><div class=\"modal-header\"><h4 class=\"modal-title\" id=\"myModalLabel\">Modal title</h4></div><div class=\"modal-body\"><h3>Modal Body</h3></div></div></div></div>"
            inRow += 1
    except Exception:
        return render(request, 'PageNotFound.html')
    else :
        return render(request, 'Hungry.html', {"HTML" : HtmlToReturn})


def State_List_API (request):

    List = {}

    StateObjects = State.objects.all()

    for obj in StateObjects:
        List[obj.name] = "api/states/" + obj.name

    return HttpResponse(json.dumps(List), content_type="application/json")



def State_ID_API (request, Pagename):
    info = {}

    try:
        obj = State.objects.get(name = Pagename)
        info["name"] = obj.name
        info["flag"] = obj.flag
        info["date_founded"] = obj.date_founded
        info["population"] = obj.population
        info["size(sqml)"] = obj.size
        info["video"] = obj.video
        parks = {}
        allparks = Park.objects.filter(state=obj)
        for p in allparks:
            parks[p.name] = "api/parks/" + p.name

        info["parks"] = parks

    except Exception:
        h = HttpResponse(json.dumps({"error": Pagename+" does not exist in the file"}), content_type="application/json")
        h.status_code = 404
        return h

    else:
        return HttpResponse(json.dumps(info), content_type="application/json")


def Park_List_API (request):
    List = {}

    ParkObjects = Park.objects.all()

    for obj in ParkObjects:
        List[obj.name] = "api/parks/" + obj.name

    return HttpResponse(json.dumps(List), content_type="application/json")

def Park_ID_API (request,Pagename):
    info = {}

    try:
        obj = Park.objects.get(name=Pagename)
        info["name"] = obj.name

        info["state"] = obj.state.name

        info["size(acre)"] = obj.size
        info["max_elevation(ft)"] = obj.max_elevation
        info["date_founded"] = obj.date_founded
        info["image"] = obj.park_image
        info["visitors(annual)"] = obj.num_visitors
        info["video"] = obj.video
        hikes = {}
        allhikes = Hike.objects.filter(park=obj)
        for h in allhikes:
            hikes[h.name] = "api/hikes" + h.name

        info["hikes"] = hikes

    except Exception:
        e = HttpResponse(json.dumps({"error": Pagename+" does not exist in the file"}), content_type="application/json")
        e.status_code = 404
        return e
    else:

        return HttpResponse(json.dumps(info), content_type="application/json")


def Hike_List_API (request):
    List = {}

    HikeObjects = Hike.objects.all()

    for obj in HikeObjects:
        List[obj.name] = "api/hikes/" + obj.name

    return HttpResponse(json.dumps(List), content_type="application/json")

def Hike_ID_API (request, Pagename):
    info = {}
    try:
        obj = Hike.objects.get(name=Pagename)
        info["name"] = obj.name
        info["distance(mile)"] = obj.distance
        info["est_time(min)"] = obj.est_time
        info["image"] = obj.hike_image
        info["difficulty"] = obj.difficulty
        info["park"] = obj.park.name
    except Exception:
        e = HttpResponse(json.dumps({"error": Pagename+" does not exist in the file"}), content_type="application/json")
        e.status_code = 404
        return e
    else:
        return HttpResponse(json.dumps(info), content_type="application/json")



def State_List (request):
    """
    Renders and returns the handle page for publishing. Uses a dictionary for all
    the variables marked for django in Handle.html or PageNotFound.html.
    """
    HtmlToReturn = "<div class=\"row\">"
    try:
        StateObjects = State.objects.all()
        statesByAlpha = sorted([state.name for state in StateObjects])
        inRow = 0
        for state in statesByAlpha :
            # if (inRow == 3) :
            #     HtmlToReturn += "</div> <div class=\"row\">"
            #     inRow = 0
            HtmlToReturn += "<div class=\"col-lg-4 col-sm-6 col-xs-12\"><a href=/states/" + state.replace(" ", "%20") + "><img src=\"" + State.objects.get(name=state).flag + "\" class=\"thumbnail img-responsive\"><div class=\"homepage\"><h2>" + state +  "</h2></a></div></div>"
            inRow += 1
    except Exception:
        return render(request, 'PageNotFound.html')
    else :
        return render(request, 'StateList.html', {"HTML" : HtmlToReturn})

def State_ID (request, Pagename):
    """
    Renders and returns the handle page for publishing. Uses a dictionary for all
    the variables marked for django in Handle.html or PageNotFound.html.
    """
    try:
        StateObject = State.objects.get(name=Pagename)
        ParksinState = Park.objects.filter(state=StateObject)
        HtmlParks = ""
        Dict = {}
        Dict["HTML_BEGIN"] = HTML_BEGIN
        Dict["name"] = StateObject.name
        Dict["date_founded"] = StateObject.date_founded
        Dict["flag"] = StateObject.flag
        Dict["population"] = locale.format("%d", StateObject.population, grouping=True)
        Dict["size"] = locale.format("%d", StateObject.size, grouping=True)
        Dict["video"] = StateObject.video
        for park in ParksinState :
            newParkName = park.name.replace(" ", "%20")
            HtmlParks += "<li><h3><a href=/parks/" + newParkName + ">" + park.name + "</a></h3></li>"
        Dict["HtmlParks"] = HtmlParks

        #getting random background
        images = []
        for filename in os.listdir("/home/Twistory/Twistory/static/images/"):
            images.append(filename)
        r = random.randint(0, len(images)-1)
        Dict["background"] = str(images[r])

    except Exception:
        return render(request, 'PageNotFound.html')
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
        parksByAlpha = sorted([park.name for park in ParkObjects])
        inRow = 0
        HtmlToReturn = "<div class=\"row\">"
        for park in parksByAlpha :
            # if (inRow == 3) :
            #     HtmlToReturn += "</div> <div class=\"row\">"
            #     inRow = 0
            HtmlToReturn += "<center><div class=\"col-lg-4 col-sm-6 col-xs-12\"><a href=/parks/" + park.replace(" ", "%20") + "><img src=\"" + Park.objects.get(name=park).park_image + "\" class=\"thumbnail img-responsive\"><div class=\"homepage\"><h2>" + park +  "</h2></a></div></div></center>"
            inRow += 1
    except Exception:
        return render(request, 'PageNotFound.html')
    else :
        return render(request, 'ParkList.html', {"HTML" : HtmlToReturn})


def Park_ID (request, Pagename):
    """
    Renders and returns the handle page for publishing. Uses a dictionary for all
    the variables marked for django in Handle.html or PageNotFound.html.
    """

    try:
        ParkObject = Park.objects.get(name=Pagename)
        HikesinPark = Hike.objects.filter(park=ParkObject)
        HtmlHikes = ""
        Dict = {}
        Dict["HTML_BEGIN"] = HTML_BEGIN
        Dict["state"] = "<a href=/states/" + ParkObject.state.name + ">" + ParkObject.state.name + "</a>"
        Dict["name"] = ParkObject.name
        Dict["size"] = locale.format("%d", ParkObject.size, grouping=True)
        Dict["max_elevation"] = locale.format("%d", ParkObject.max_elevation, grouping=True)
        Dict["date_founded"] = ParkObject.date_founded
        Dict["park_image"] = ParkObject.park_image
        Dict["num_visitors"] = locale.format("%d", ParkObject.num_visitors, grouping=True)
        Dict["video"] = ParkObject.video
        for hike in HikesinPark :
            HtmlHikes += "<li><h3><a href=/hikes/" + hike.name.replace(" ", "%20") + ">" + hike.name + "</a></h3></li>"
        Dict["HtmlHikes"] = HtmlHikes

        #getting random background
        images = []
        for filename in os.listdir("/home/Twistory/Twistory/static/images/"):
            images.append(filename)
        r = random.randint(0, len(images)-1)
        Dict["background"] = str(images[r])

    except Exception:
        return render(request, 'PageNotFound.html')
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
        hikesByAlpha = sorted([hike.name for hike in HikeObjects])
        inRow = 0
        HtmlToReturn = "<div class=\"row\">"
        for hike in hikesByAlpha :
            # if (inRow == 3) :
            #     HtmlToReturn += "</div> <div class=\"row\">"
            #     inRow = 0
            HtmlToReturn += "<center><div class=\"col-lg-4 col-sm-6 col-xs-12\"><a href=/hikes/" + hike.replace(" ", "%20") + "><img src=\"" + Hike.objects.get(name=hike).hike_image + "\" class=\"thumbnail img-responsive\"><div class=\"homepage\"><h2>" + hike +  "</h2></a></div></div></center>"
            inRow += 1
    except Exception:
        return render(request, 'PageNotFound.html')
    else :
        return render(request, 'HikeList.html', {"HTML" : HtmlToReturn})

def Hike_ID (request, Pagename):
    """
    Renders and returns the handle page for publishing. Uses a dictionary for all
    the variables marked for django in Handle.html or PageNotFound.html.
    """
    try:
        HikeObject = Hike.objects.get(name=Pagename)
        Dict = {}
        Dict["HTML_BEGIN"] = HTML_BEGIN
        Dict["name"] = HikeObject.name
        Dict["distance"] = HikeObject.distance
        Dict["est_time"] = HikeObject.est_time
        Dict["hike_image"] = HikeObject.hike_image
        Dict["difficulty"] = HikeObject.difficulty
        Dict["park"] = "<h3><a href=/parks/" + HikeObject.park.name.replace(" ", "%20") + ">" + HikeObject.park.name + "</a></h3>"

        #getting random background
        images = []
        for filename in os.listdir("/home/Twistory/Twistory/static/images/"):
            images.append(filename)
        r = random.randint(0, len(images)-1)
        Dict["background"] = str(images[r])

    except Exception:
        return render(request, 'PageNotFound.html')
    else :
        return render(request, 'Hike.html', Dict)

def Search (request) :
    query_string = ''
    sqs_list = []
    sqs_or = set()
    same_results = set()
    and_names = set()
    or_names = set()
    final_sqs_or = set()

    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        new_query = query_string.split(' ')
        for word in new_query :
            sqs_list.append((SearchQuerySet().filter(content=word)))
        for curSet in sqs_list :
            sqs_or.update(set((q for q in curSet)))

        sqs_and = set(SearchQuerySet().filter(content=query_string))

        for item in sqs_and :
            and_names.add(item.name)
        for item in sqs_or :
            or_names.add(item.name)

        same_results = and_names.intersection(or_names)

        for item in sqs_or :
            if item.name not in same_results :
                final_sqs_or.add(item)


    return render_to_response('search/search.html', {'and_results': sqs_and, 'or_results' : final_sqs_or, 'query' : query_string, 'same_results' : same_results})