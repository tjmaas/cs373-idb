from django.conf.urls import patterns, include, url
from Twistory.myapp.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Twistory.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homepage),
    url(r'^ErikSpoelstra/$', ErikSpoelstra),
    url(r'^LeBronJames/$', LeBronJames),
    url(r'^GreggPopovich/$', GreggPopovich),
    url(r'^ChrisBosh/$', ChrisBosh),
    url(r'^DwyaneWade/$', DwyaneWade),
)
