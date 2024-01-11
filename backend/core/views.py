from django.shortcuts import render
from django.views import generic
from core.models import Todo
from core.serializers import TodoSerializers
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class HomeViewr(generic.TemplateView):
    template_name= 'home.html'


class TodoViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        todoList = Todo.objects.all().order_by('id').values()

        dodoListSerializer = TodoSerializers(todoList, many=True)

        return Response(dodoListSerializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        content = request.data.get('content')

        if content:
            data = {
                "content": content
            }

            serializer = TodoSerializers(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response({'msg': 'content não achado'}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        id = request.data.get('id')

        if id:
            try:
                todo = Todo.objects.get(id=id)
            except Todo.DoesNotExist:
                todo = None     

            data = {
                'content': request.data.get('content') if request.data.get('content') else todo.content,
                'finished': request.data.get('finished') if request.data.get('finished') else todo.finished,
            }

            serializer = TodoSerializers(instance=todo, data=data, partial=True)

            if todo and serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response({'msg': 'id ou content não encontrado'}, status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request):
        id = request.data.get('id')

        if id:
            try:
                todo = Todo.objects.get(id=id)
            except Todo.DoesNotExist:
                todo = None
            
            if todo:
                todo.delete()
                return Response({'msg': "todo deletado"}, status=status.HTTP_200_OK)
            
        return Response({'msg': 'todo não achado'}, status=status.HTTP_400_BAD_REQUEST)



