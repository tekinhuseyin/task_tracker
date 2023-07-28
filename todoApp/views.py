from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *

from.models import Todo
from .serializers import TodoSerializer

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )

@api_view(["GET","POST"])
def todo_list_create(request):
    if request.method=="GET":
        todos=Todo.objects.all()                       #todo todo modelimin hepsi gelsin. 
        serializer=TodoSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message={"message":"Successfully Created"}
            return Response(message, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@