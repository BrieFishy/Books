from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator


# Create your views here.
def book_list(request):
    books_list = Book.objects.all()
    book_name = request.GET.get('book_name')
    if book_name != '' and book_name is not None:
        books_list = books_list.filter(book_name__icontains=book_name)
    paginator = Paginator(books_list, 5)
    page = request.GET.get('page')
    books_list = paginator.get_page(page)
    return render(request, 'book.html', {'book_list': books_list})

