from django.shortcuts import render, redirect
from django.views import View
from .models import Book
from .forms import BookForm
# Create your views here.

# class Index(View):
#     def get(self, request):
#         return render(request, "index.html")
    
class BookView(View):
    def get(self, request):
        form = BookForm()
        books = Book.objects.all()
        context = {
            'books': books,
            'form': form,
        }
        return render(request, "index.html", context)
    
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("bookview")
    
class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        context = {
            'book': book
        }
        return render(request, "detailview.html", context)
    
class BookDeleteView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()
        return redirect("bookview")