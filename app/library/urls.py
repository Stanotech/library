from django.urls import path
from .views import LibraryView

urlpatterns = [
    path("books", LibraryView.as_view(), name="book-list"),
    path("book/<int:book_id>", LibraryView.as_view(), name="book-detail")
]