from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.models import *
from app.serializers import *
# Create your views here.


class StudentCrud(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    


