from django.conf.urls import *
from myapp.views import *


from django.contrib import admin
#admin.autodiscover()

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
    url(r'^search/', Search),


    # API
    url(r'^api/states/$', State_List_API),
    url(r'^api/states/(.*)/$', State_ID_API),
    url(r'^api/parks/$', Park_List_API),
    url(r'^api/parks/(.*)/$', Park_ID_API),
    url(r'^api/hikes/$', Hike_List_API),
    url(r'^api/hikes/(.*)/$', Hike_ID_API),

    url(r'^.*/$', PageNotFound)
)
