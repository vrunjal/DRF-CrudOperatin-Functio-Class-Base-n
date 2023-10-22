from rest_framework import serializers
from .models import Student


def starts_with_r(value):   #validators
    if value['0'].lower != "r":
        raise serializers.ValidationError("Name should starts withr R")
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=70)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=70)
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    def update(self,instance,validated_data):                 #instance-old data that is already present,validated_data-that is coming from user which will be updated
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    def validate_roll(self,value):   #Field leval validation(Single object)
        if value >=200:
            raise serializers.ValidationError("Seat Full")
        return value
    
    def validate(self,value):       #object level validation(Multiple Objects)
        nm=value.get("name")
        ct=value.get("city")
        if nm.lower() == "rohit" and ct.lower() != "ranchi":
            raise serializers.ValidationError("City must be ranchi")
        return value