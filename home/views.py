from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import StudentSerializer
from rest_framework import serializers, status
from .models import Student
# Create your views here.
@api_view(['GET'])
def ApiView(request):
    api_urls = {
    'all students' : '/',
    'Add' : '/create',
    'Update' : '/Update/pk',
    'Delete' : 'pk/delete'
    }

    return Response(api_urls)

@api_view(['POST'])
def Add(request):
    data = request.data
    serializer = StudentSerializer(data = data)

    if Student.objects.filter(**data).exists():
        raise serializers.ValidationError('Already Exists')
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def AllStudents(request):
    students = Student.objects.all()
    if students:
        serializer = StudentSerializer(students,many = True)
        return Response(serializer.data)
    else: 
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def Update(request,pk):
    if Student.objects.filter(pk = pk).exists():
        student = Student.objects.get(pk = pk)
        data = StudentSerializer(instance=student,data = request.data)

        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)