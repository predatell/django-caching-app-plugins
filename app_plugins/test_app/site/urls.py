from django.conf.urls.defaults import *

urlpatterns = patterns('plugintest.site.views',
    (r'^$', 'index_page'),
)