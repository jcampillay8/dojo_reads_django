from django.urls import path
from . import views

urlpatterns = [
    path('book', views.book),
#     path('books/add', views.add_book),
#     path('logout', views.logout),
#     path('book/<int:book_id>', views.one_book),
#     path('add_review', views.add_review),
#     path('delete/<int:review_id>/<int:book_id>', views.delete_review),
#     path('users/<int:id>', views.user),
]
