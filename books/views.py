from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from books.models import *
from .forms import *
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
def book_list(request):
    books = Book.objects.order_by('-pub_date')
    genres = Book.GenreType
    items_per_page = 12
    paginator = Paginator(books, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'books/book_list.html', {'page': page, 'genres': genres})


def books_by_genre(request, genre_type):
    books = Book.objects.filter(genre=genre_type)
    return render(request, 'books/genresort.html', {'genre_type': genre_type, 'books': books})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = Review.objects.filter(book=book)
    similar_books = Book.objects.filter(genre=book.genre).exclude(id=book.id)[:3]
    similar_books_data = [{'title': book.title, 'url': reverse('book_detail', args=[book.id])} for book in similar_books]
    chapters = Chapter.objects.filter(book=book)
    return render(request, 'books/book_detail.html', {'book': book, 'reviews': reviews, 'similar_books_data': similar_books_data, 'chapters': chapters})

def add_chapter(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.book = book
            chapter.save()
            return redirect('book_detail', id=id)
    else:
        form = ChapterForm()

    return render(request, 'books/add_chapter.html', {'form': form, 'book': book})


def submit_review(request, id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=id)
        creator = request.user
        ratings = request.POST.get('ratings')
        comment = request.POST.get('comment')
        review = Review.objects.create(creator=creator, book=book, ratings=ratings, comment=comment)
        return redirect('book_detail', id=id)
    return HttpResponseBadRequest()


def book_search(request):
    if 'query' in request.GET:
        query = request.GET['query']
        results = Book.objects.filter(title__icontains=query)
    else:
        results = None

    form = BookSearchForm()

    return render(request, 'books/search.html', {'results': results, 'form': form})


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'contributors', 'isbn', 'pub_date', 'image', 'genre', 'pdf_file']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = True
        # context['available_genres'] = Genre.GenreType
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# class ChapterCreateView(LoginRequiredMixin, CreateView):
#     model = Chapter
#     form_class = ChapterForm
#     template_name = 'add_chapter'


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'contributors', 'isbn', 'pub_date', 'image', 'genre', 'pdf_file']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = False
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.author:
            return True
        return False

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/book_list/'

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.author:
            return True
        return False
