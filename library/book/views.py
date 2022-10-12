from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

# Create your views here.

def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/library.html', {'shelf': shelf})
    
def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse(""" Something went wrong. Please reload the webpage by clicking <a href="{{url:'index'}}>Reload</a>" """)
    else:
        return render(request, 'book/upload_form.html', {'upload_form': upload})
