from django.contrib.auth.mixins import LoginRequiredMixin
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
	template_name = 'book_list.html'
	paginate_by = 25


class BookDetailView(LoginRequiredMixin, DetailView):
	model = Book
	template_name = 'book_detail.html'


class AuthorListView(ListView):
	model = Author
	template_name = 'authors.html'
	paginate_by = 25


class AuthorDetailView(LoginRequiredMixin, DetailView):
	model = Author
	template_name = 'author_detail.html'


class LoanedBookUserListView(LoginRequiredMixin, ListView):
	model = BookInstance
	template_name = 'borrowed_book.html'
	paginate_by = 10

	def get_queryset(self):
		return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('-due_back')