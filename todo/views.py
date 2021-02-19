from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ToDoSerializer
from .models import Todo


class ToDoListView(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = Todo.objects.all()

