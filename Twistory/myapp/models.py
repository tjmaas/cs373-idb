from django.db import models

# Create your models here.

class Handle(models.Model) :
    """
    Model class for handles.  Used to describe users in twitter and contain
    values useful for our database.
    """
    picture = models.ImageField()
    username = models.CharField(max_length = 50) # primary key?
    name = models.CharField(max_length = 50)
	#video = models.FileField(upload_to = u'video/', max_length=200)
    bio = models.CharField(max_length = 100)
    graph = models.ImageField()
    tweets = models.TextField(null = True)

class Hashtag(models.Model) :
    """
    Model class for hashtags.  Used to describe indicated strings by users
    to label their tweets with.  Used to describe attributes of these hashtags.
    """
    name = models.CharField(max_length = 50) # primary key?
    graph = models.ImageField()
    description = models.CharField(max_length = 50)
    popular_users = models.TextField(null = True)

class Cluster(models.Model) :
    """
    Cluster class for clusters.  Used to describe related hashtags and their
    users.
    """
    name = models.CharField(max_length = 50) # primary key?
    members = models.TextField(null = True)
    parents = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    key_figures = models.TextField(null = True)
    related_pages = models.TextField(null = True)
    graphs = models.ImageField()
