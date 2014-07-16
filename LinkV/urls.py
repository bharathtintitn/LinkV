from django.conf.urls import patterns, include, url
#from views import homepagei
from views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LinkV.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', homepage),
    url(r'^register/$',registrationForm),
    url(r'^registration/$',submit),
)
