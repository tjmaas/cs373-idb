import datetime
from haystack import indexes
from myapp.models import State


class StateIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    name = indexes.CharField(model_attr='name')
    date_founded = indexes.CharField(model_attr='date_founded')
    flag = indexes.CharField(model_attr='flag')
    population = indexes.IntegerField(model_attr='name')
    size = indexes.IntegerField(model_attr='name')
    video = indexes.CharField(model_attr='video')

    def get_model(self):
        return State

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())