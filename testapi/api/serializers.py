from rest_framework import serializers
from .models import Student, StudentClass

class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = ['class_name','section']

class StudentSerializer(serializers.ModelSerializer):
    class_name = StudentClassSerializer(read_only =False)
    class Meta:
        model = Student
        fields = ['class_name','stuname','email']
        
    def update(self,instance, validated_data):
        class_name_data = validated_data.pop('class_name',None)
        print("class_name_data : ",class_name_data)
        print("instance",instance)
        if class_name_data:
            class_name_serializer = StudentClassSerializer(instance.class_name,data=class_name_data)
            if class_name_serializer.is_valid():
                class_name_serializer.save()
                
        
        instance.stuname = validated_data.get('stuname',instance.stuname)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        
        return instance