from django.shortcuts import render
from Book.models import Book

def book_info(request):
    return render(request, 'book_info.html', {'books':books})

