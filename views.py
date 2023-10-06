from django.shortcuts import render

from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView
# RetrieveAPIView
from .serializers import TodoSerializer
from todo.models import Todo

# Create your views here.



class ListTodoAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
class CreateTodoAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
class UpdateTodoAPIView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
class DeleteTodoAPIView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class RetrieveTodoAPIView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer