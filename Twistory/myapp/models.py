from django.db import models

# Create your models here.

class State(models.Model) :
    """
    Model class for States. Used to represent State data.
    """
    name = models.CharField(max_length = 255)
    date_founded = models.CharField(max_length = 10)
    flag = models.CharField(max_length = 1000)
    population = models.IntegerField()
    size = models.IntegerField()
    video = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name

class Park(models.Model) :
    """
    Model class for Park. Used to represent Park data.
    """
    state = models.ForeignKey('State', related_name = "parks")
    name = models.CharField(max_length = 255)
    size = models.IntegerField()
    max_elevation = models.IntegerField()
    date_founded = models.CharField(max_length = 255)
    park_image = models.CharField(max_length = 1000)
    date_founded = models.CharField(max_length = 10)
    park_image = models.CharField(max_length = 1000)
    num_visitors = models.IntegerField()
    video = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name

class Hike(models.Model) :
    """
    Model class for Hikes.  Used to represent Hike data.
    """
    name = models.CharField(max_length = 255)
    distance = models.FloatField()
    est_time = models.IntegerField()
    hike_image = models.CharField(max_length = 1000)
    difficulty = models.CharField(max_length = 255)
    park = models.ForeignKey('Park', related_name = "hikes")

    def __str__(self):
        return self.name
