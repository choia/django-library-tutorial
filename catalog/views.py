from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, BookInstance, Author, Genre 



def index(request):
	num_books 		= Book.objects.all().count()
	num_instances 	= BookInstance.objects.all().count()

	num_instances_available 	= BookInstance.objects.filter(status__exact='a').count()
	num_authors 				= Author.objects.all().count()

	context = {
		'num_books': num_books,
		'num_instances': num_instances,
		'num_instances_available': num_instances_available,
		'num_authors': num_authors,
	}

	return render(request, 'index.html', context)



class BookListView(ListView):
	model = Book
	paginate_by = 25
	template_name = 'book_list.html'


class BookDetailView(DetailView):
	model = Book
	template_name = 'book_detail.html'



class AuthorListView(ListView):
	model = Author
	paginate_by = 25
	template_name = 'authors.html'


class AuthorDetailView(DetailView):
	model = Author
	template_name = 'author_detail.html'


