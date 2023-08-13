# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import * 
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to Todo APP</h1></center>'
    )
#### FBV ###
@api_view(['GET','POST'])
def todo_list_create(request):
    if request.method=='GET':
        todos=Todo.objects.all()
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message={"message":"Successfully Created"}
            return Response(message,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])

def todo_get_delete_update(request,id):
    todo=get_object_or_404(Todo,id=id)

    if request.method=='GET':
        serializer=TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=TodoSerializer(data=request.data, instance=todo)
        if serializer.is_valid():
            serializer.save()
            message={"message":"Successfully Updated"}
            return Response(message,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        todo.delete()
        message={"message":"Successfully Deleted"}
        return Response(message,status=status.HTTP_202_ACCEPTED)

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
### CBV ###
class Todos(ListCreateAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

class TodosRUD(RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    # lookup_field=id

from rest_framework.viewsets import ModelViewSet
### MVS ###
class TodosMVS(ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
  
    