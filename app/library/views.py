from django.shortcuts import 
from rest_framework.response import Response
from rest_framework.views import APIView
from library.models import Book
from library.serializers import BookSerializer

class LibraryView(ApiView):
    def get(self, request):
        books = Book.objects.all()
        return Response({"books": books})
    
class BookDetailView(ApiView):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data, content_type="application/json")
