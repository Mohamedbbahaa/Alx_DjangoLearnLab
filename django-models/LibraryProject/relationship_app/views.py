from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books' : books})
# Create your views here.

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        # Get the existing context data from DetailView
        context = super().get_context_data(**kwargs)
        # Add books related to this library to the context
        context['books'] = self.object.books.all()
        return context
