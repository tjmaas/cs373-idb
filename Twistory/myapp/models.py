from django.db import models

# Create your models here.

class Handle(models.Model) :
	picture = models.ImageField()
	username = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	bio = models.CharField(max_length = 100)
	graph = models.ImageField()
	tweets = models.TextField(null = True)

class Hashtag(models.Model) :
	name = models.CharField(max_length = 50)
	graph = models.ImageField()
	description = models.CharField(max_length = 50)
	popular_users = models.TextField(null = True)

class Cluster(models.Model) :
	name = models.CharField(max_length = 50)
	members = models.TextField(null = True)
	parents = models.CharField(max_length = 50)
	timeline = models.ImageField()
	description = models.CharField(max_length = 100)
	key_figures = models.TextField(null = True)
	related_pages = models.TextField(null = True)
	graphs = models.ImageField()
