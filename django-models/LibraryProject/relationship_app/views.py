from django.shortcuts import render
from relationship_app.models import Book, Library
from django.views.generic import DetailView

def book_list_view(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/book_list.html', {'books' : books})
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
