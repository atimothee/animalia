from django.conf.urls import patterns, include, url
from django.contrib import admin
from animalia import settings
from catalog.views import AnimalDetail

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'catalog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^animals/list$', 'catalog.views.animal_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^id/(?P<pk>[-_\w]+)/$', AnimalDetail.as_view()),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))