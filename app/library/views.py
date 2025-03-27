from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from datetime import date

from library.models import Book
from library.serializers import BookSerializer

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class LibraryView(APIView):
    def get(self, request):

        books = Book.objects.all()
        author = request.query_params.get('author', None)
        if author:
            books = books.filter(author__icontains=author)

        paginator = CustomPagination()
        paginated_books = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(paginated_books, many=True)

        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        if len(request.data.get("isbn")) != 13:
            return Response({"error": "ISBN must be 13 characters long"}, status=status.HTTP_400_BAD_REQUEST)
        actual_date = str(date.today())
        if request.data.get("published_date") >= actual_date:
            return Response({"error": "Published date must be in the past"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookDetailView(APIView):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, book_id):
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, book_id):
        book = Book.objects.get(id=book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
