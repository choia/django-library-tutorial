from datetime import date, timedelta
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, BookInstance, Author, Genre 
from .forms import RenewBookForm


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


class AllBorrowedBookListView(PermissionRequiredMixin, ListView):
	model = BookInstance
	template_name = 'all_borrowed_book.html'
	paginate_by = 25
	permission_required = 'catalog.can_mark_returned'



def renew_book(request, pk):
	book_instance = get_object_or_404(BookInstance, pk=pk)

	if request.method == 'POST':
		form = RenewBookForm(request.POST)

		if form.is_valid():
			book_instance.due_back = form.cleaned_data['renewal_date']
			book_instance.save()

			return HttpResponseRedirect(reverse('all-borrowed-book'))

	else:
		proposed_renewal_date = date.today() + timedelta(weeks=3)
		form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})		

	context = {
		'form': form,
		'book_instance': book_instance,
	}	

	return render(request, 'renew_book.html', context)



class AuthorCreate(PermissionRequiredMixin, CreateView):
	model = Author
	template_name = 'author_form.html'
	fields = '__all__'
	permission_required = 'catalog.can_mark_returned'
	

class AuthorUpdate(PermissionRequiredMixin, UpdateView):
	model = Author
	template_name = 'author_form.html'
	fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
	permission_required = 'catalog.can_mark_returned'


class AuthorDelete(PermissionRequiredMixin, DeleteView):
	model = Author
	template_name = 'author_confirm_delete.html'
	success_url = reverse_lazy('authors')
	permission_required = 'catalog.can_mark_returned'