from django.urls import path

from library.views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path("books", BookListCreateView.as_view(), name="book-list"),
    path("book/<int:pk>", BookRetrieveUpdateDestroyView.as_view(), name="book-detail")
]