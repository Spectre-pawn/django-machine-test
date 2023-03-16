from django.http import  HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer


def index(request):
    return HttpResponse("welcome")


@api_view(['GET'])
def client_list(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def client_create(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def client_detail(request, pk):
    client = Client.objects.get(pk=pk)
    serializer = ClientSerializer(client)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def client_update(request, pk):
    client = Client.objects.get(pk=pk)
    serializer = ClientSerializer(client, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def client_delete(request, pk):
    client = Client.objects.get(pk=pk)
    client.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def project_create(request, pk):
    client = Client.objects.get(pk=pk)
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(client=client, created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def project_list(request):
    projects = Project.objects.filter(users=request.user)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)
