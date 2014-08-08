from django.conf.urls import patterns, url, include
from Twistory.myapp.views import *
# from haystack.views import SearchView
# from haystack.forms import SearchForm
from haystack.query import SearchQuerySet


sqs = SearchQuerySet()

from django.contrib import admin
from Twistory.myapp.models import State,Hike,Park
admin.autodiscover()
admin.site.register(State)
admin.site.register(Hike)
admin.site.register(Park)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Twistory.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^about/$', About),
    url(r'^states/$', State_List),
    url(r'^states/(.*)/$', State_ID),
    url(r'^parks/$', Park_List),
    url(r'^parks/(.*)/$', Park_ID),
    url(r'^hikes/$', Hike_List),
    url(r'^hikes/(.*)/$', Hike_ID),
    url(r'^hungry/$', Hungry),
    url(r'^$', Homepage),
    # url(r'^search/$', SearchView(
    #     template='search/search.html',
    #     searchqueryset=sqs,
    #     form_class=SearchForm),
    #     name='haystack_search'),
    url(r'^search/$', Search),


    # API
    url(r'^api/states/$', State_List_API),
    url(r'^api/states/(.*)/$', State_ID_API),
    url(r'^api/parks/$', Park_List_API),
    url(r'^api/parks/(.*)/$', Park_ID_API),
    url(r'^api/hikes/$', Hike_List_API),
    url(r'^api/hikes/(.*)/$', Hike_ID_API),

    url(r'^.*/$', PageNotFound)
)
# SearchView(
#         template='search/search.html',
#         searchqueryset=sqs,
#         form_class=HighlightedSearchForm),
#         name='haystack_search')