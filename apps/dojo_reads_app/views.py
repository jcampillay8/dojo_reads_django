from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def book(request):
    # if 'id' in request.session:
    #     context = {
    #         'user': User.objects.get(id=request.session['id']),
    #         'postedMessages' : Message.objects.all(),
    #         'postedComments' : Comment.objects.all(),
    #     }
    #     print('user is in session')
    #     return render(request, 'thewall/wall.html', context)
    # return redirect('/')
    if 'first_name' in request.session:
        context={
            'last_3_reviews': Review.objects.all().order_by('-id')[:3],
            'all_books': Book.objects.all()
        }
        return render(request, 'books/books_home.html', context)
    return render(request,'books/books_home.html')

def add_book(request):
    context = {
        'all_authors': Author.objects.all()
    }
    if request.method == 'POST':
        existing_author = Author.objects.filter(author=request.POST['author'])
        if len(existing_author) > 0:
            this_author = existing_author[0]
        else:
            this_author = Author.objects.create(author=request.POST['new_author'])
        book = Book.objects.create(title=request.POST['title'], author=this_author)
        Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book=book, poster=User.objects.get(id=request.session['id']))
        book_id = book.id
        return redirect(f'/book/{book_id}')
    return render(request, 'books/add_book.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def one_book(request, book_id):
    book = Book.objects.get(id=book_id)
    context ={
        'book': Book.objects.get(id=book_id),
        'all_reviews': book.reviews.all()
    }
    return render(request, 'books/one_book.html', context)

def add_review(request):
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_user = User.objects.get(id=request.session['id'])
    book_id = request.POST['book_id']
    if len(request.POST['review']) < 5:
        messages.error(request, "Review must be at least 5 characters!")
        return redirect(f'/book/{book_id}')
    Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book=this_book, poster=this_user)
    return redirect(f'/book/{book_id}')

def delete_review(request, review_id, book_id):
    review_to_delete = Review.objects.get(id=review_id)
    review_to_delete.delete()
    return redirect(f'/book/{book_id}')

def delete_book(request, book_id):
    book_to_delete = Book.objects.get(id=book_id)
    book_to_delete.delete()
    return redirect('/book/book')

def user(request, id):
    current_user = User.objects.get(id=id)
    # user_reviews = current_user.reviews.all()
    # print(user_reviews[0].book.title)
    context={
        'user': current_user,
        'user_reviews': current_user.reviews.all()
    }
    return render(request, 'books/user.html', context)
