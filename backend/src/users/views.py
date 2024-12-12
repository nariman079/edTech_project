from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser

# Детальная информация о пользователе 
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'full_name', 'student_class', 'mail']

class CustomUserRetrieveAPIView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

