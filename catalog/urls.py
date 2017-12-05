from django.conf.urls import include, url
from . import views


# Application URL Mapper
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]

# User Loaned Book URL Conf
urlpatterns += [
	url(r'^mybooks/$', views.LoanedBookUserListView.as_view(), name='borrowed-book'),
	url(r'^borrowed/$', views.AllBorrowedBookListView.as_view(), name='all-borrowed-book'),
]

# Renew Book URL Conf
urlpatterns += [
	url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book, name='renew-book'),
]