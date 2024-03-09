from rest_framework import serializers
from app.models import *

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        

