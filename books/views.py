from django.shortcuts import render, get_object_or_404
from .models import Genre, Book, Author,
from cart.forms import CartAddProductForm


def book_list(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    books = Book.objects.filter(available=True)
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = books.filter(genre=genre)
    return render(request, 'books/book/list.html', {'genre': genre,
                                                      'genres': genres,
                                                      'books': books})
def author_list(request, author_slug=None):
    author = None
    authors = Author.objects.all()
    books = Book.objects.filter(available=True)
    if author_slug:
        author = get_object_or_404(Author, slug=author_slug)
        books = books.filter(author=author)
    return render(request, 'books/book/list.html', {'author': author, 'authors': authors, 'books' : books })

def book_detail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug, available=True)
    cart_book_form = CartAddProductForm()
    return render(request, 'books/book/detail.html', {'book': book, 'cart_book_form': cart_book_form})
