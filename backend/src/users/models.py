from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    student_class = models.CharField(max_length=10, verbose_name="Класс")
    mail = models.EmailField(unique=True, verbose_name="Электронная почта")

    def __str__(self):
        return self.username