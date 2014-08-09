from haystack import indexes
from .models import State, Park, Hike


class StateIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)

    name = indexes.NgramField(model_attr='name')
    date_founded = indexes.CharField(model_attr='date_founded')
    flag = indexes.CharField(model_attr='flag')
    population = indexes.IntegerField(model_attr='population')
    size = indexes.IntegerField(model_attr='size')
    video = indexes.CharField(model_attr='video')
    content_auto = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return State


    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class ParkIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)

    content_auto = indexes.EdgeNgramField(model_attr='state')
    # state = indexes.CharField()
    name = indexes.CharField(model_attr='name')
    size = indexes.IntegerField(model_attr='size')
    max_elevation = indexes.IntegerField(model_attr='max_elevation')
    date_founded = indexes.CharField(model_attr='date_founded')
    park_image = indexes.CharField(model_attr='park_image')
    num_visitors = indexes.IntegerField(model_attr='num_visitors')
    def get_model(self):
        return Park

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class HikeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)

    name = indexes.CharField(model_attr='name')
    distance = indexes.FloatField(model_attr='distance')
    est_time = indexes.IntegerField(model_attr='est_time')
    hike_image = indexes.CharField(model_attr='hike_image')
    difficulty = indexes.CharField(model_attr='difficulty')
    park = indexes.CharField()

    def get_model(self):
        return Hike

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

