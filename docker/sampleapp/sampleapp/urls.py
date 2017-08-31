from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'sampleapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('sample.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
