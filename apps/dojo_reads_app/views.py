from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def book(request):
    pass
    # if 'first_name' in request.session:
    #     context={
    #         'last_3_reviews': Review.objects.all().order_by('-id')[:3],
    #         'all_books': Book.objects.all()
    #     }
    #     return render(request, 'books/books_home.html', context)
    # return render(request,'books/books_home.html')