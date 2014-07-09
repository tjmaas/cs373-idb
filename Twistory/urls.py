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
    url(r'^Handles/(.*)/$', Handle),
    url(r'^Hashtags/(.*)/$', Hashtag),
    url(r'^Clusters/(.*)/$', Cluster),
    url(r'^.*/$', Homepage)
)
