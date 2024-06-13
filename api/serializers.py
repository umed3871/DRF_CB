from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll_no = serializers.IntegerField()
    course = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # print(instance.name) #print existing name
        instance.id = validated_data.get('id', instance.name)
        instance.name = validated_data.get('name', instance.name)
        # print(instance.name) # print updated name
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.course = validated_data.get('course', instance.course)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance