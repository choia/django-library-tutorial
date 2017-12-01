from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^authors/$', views.authors, name='authors'),
    url(r'^books/$', views.books, name='books'),
]