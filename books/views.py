from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Book
from .serializer import BookSerializer
from .permissions import PermissionsClass
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BooksListView(ListAPIView, CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (PermissionsClass, IsAuthenticated)

class BookDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (PermissionsClass, IsAuthenticated)
    