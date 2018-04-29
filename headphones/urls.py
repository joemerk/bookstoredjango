from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.headphone_list, name='headphone_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.headphone_list, name = 'headphone_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.headphone_detail, name = 'headphone_detail'),
]