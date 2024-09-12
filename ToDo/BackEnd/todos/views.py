from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerailizer
# Create your views here.

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerailizer
    
class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerailizer


