from django.contrib import admin
from .models import Book, BookInstance, Author, Genre


admin.site.register(Genre)


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Author, AuthorAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('book', 'status', 'borrower', 'due_back', 'imprint')
	list_filter = ('status', 'due_back')

	fieldsets = (
		(None, {
			'fields': ('book', 'id', 'imprint')
			}),
		('Availability', {
			'fields': ('status', 'due_back', 'borrower')
			})
	)
