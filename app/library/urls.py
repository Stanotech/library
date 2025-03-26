from django.urls import path

from library.views import LibraryView, BookDetailView

urlpatterns = [
    path("books", LibraryView.as_view(), name="book-list"),
    path("book/<int:book_id>", BookDetailView.as_view(), name="book-detail")
]