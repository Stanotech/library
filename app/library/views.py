from django.shortcuts import 
from rest_framework.response import Response
from rest_framework.views import APIView
from library.models import Book

class LibraryView(ApiView):
    def get(self, request):
        books = Book.objects.all()
        return Response({"books": books})