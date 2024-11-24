from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from bookshelf.models import Book
from .forms import SearchForm

def search_books(request):
    form = SearchForm(request.GET or None)
    books = []
    if form.is_valid():
        search_term = form.cleaned_data['search_term']
        books = Book.objects.filter(title__icontains=search_term)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})

@csrf_protect
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@csrf_protect
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'bookshelf/create_book.html')

@csrf_protect
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@csrf_protect
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return HttpResponse("Book deleted")
    return render(request, 'bookshelf/confirm_delete.html', {'book': book})