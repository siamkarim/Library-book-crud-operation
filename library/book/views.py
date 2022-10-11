from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

# Create your views here.

def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/library.html', {'shelf': shelf})
