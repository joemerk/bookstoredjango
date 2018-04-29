from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.book_list, name='book_list'),
	url(r'^(?P<author_slug>[-\w]+)/$', views.author_list, name = 'book_list_by_author'),
    url(r'^(?P<genre_slug>[-\w]+)/$', views.book_list, name = 'book_list_by_genre'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.book_detail, name = 'book_detail'),
]