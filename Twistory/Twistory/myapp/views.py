from django.http import HttpResponse
from django.shortcuts import render

import datetime

def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request):
	now = datetime.datetime.now()
	return render(request, 'current_datetime.html', {'current_date' : now })

def homepage(request):
	image_data = "http://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&docid=EezbEmUu5i9I_M&tbnid=lFLmV81p9vpIlM:&ved=0CAUQjRw&url=http%3A%2F%2Fabcnews.go.com%2FSports%2Fchris-bosh-slurs-banned%2Fstory%3Fid%3D22685799&ei=2E27U9fIJobJ8wHY94CoCw&bvm=bv.70138588,d.b2U&psig=AFQjCNFiQVSJh3L5HIM9etLNS6sKW0H2HA&ust=1404870479140569"
	return render(request, 'current_datetime.html', {'img_addr' : image_data })
