from django.db.models import fields
from rest_framework import serializers
from home.models import Student
from django.contrib.auth.models import User

class UserSeriliazer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name','rollno','std')
