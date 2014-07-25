from django.conf.urls import patterns, include, url
from Twistory.myapp.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Twistory.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Homepage),
    url(r'^about/$', About),
    url(r'^states/$', State_List),
    url(r'^api/states/$', State_List_API),
    url(r'^api/states/(.*)/$', State_ID_API),
    url(r'^states/(.*)/$', State_ID),
    url(r'^parks/$', Park_List),
    url(r'^parks/(.*)/$', Park_ID),
    url(r'^api/parks/$', Park_List_API),
    url(r'^api/parks/(.*)/$', Park_ID_API),
    url(r'^hikes/$', Hike_List),
    url(r'^hikes/(.*)/$', Hike_ID),
    url(r'^api/hikes/$', Hike_List_API),
    url(r'^api/hikes/(.*)/$', Hike_ID_API),
    url(r'^.*/$', PageNotFound)
)
