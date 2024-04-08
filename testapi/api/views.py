from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .serializers import StudentSerializer
from .models import Student
class StudentApiView(APIView): 
    def get (self,request,*args,**kwargs):
        email = "robin2@email.com"
        student = Student.objects.get(email=email)
        serializer = StudentSerializer(student)

        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
            email = "robin2@email.com"  # Assuming you have 'pk' as the primary key parameter in your URL
            try:
                student = Student.objects.get(email=email)
                serializer = StudentSerializer(student, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': f'Error updating student: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
