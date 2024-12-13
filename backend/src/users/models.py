from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class CustomUserManager(BaseUserManager):

    def create_user(
        self, 
        username,
        email,
        first_name,
        last_name,
        password=None
    ):
        if not email or username:
            raise ValueError("Обязательное поле")

        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(
        self, 
        username: str, 
        email,
        first_name=None,
        last_name=None,
        password=None
        ):
        
        if not (email and username):
            raise ValueError("Обязательное поле")

        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Пользователь
    """

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    username = models.CharField(
        max_length=20,
        unique=True,
        null=True, blank=True,
        verbose_name='Логин',
        error_messages={
            'unique': "Такой username ученика уже существует"
        }
    )
    email = models.CharField(
        max_length=30, 
        unique=True,
        null=True, blank=True,
        verbose_name="Почта",
        error_messages={
            'unique': "Такой email ученика уже существует"
        }
    )
    first_name = models.CharField(
        max_length=20,
        null=True, blank=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=20,
        null=True, blank=True,
        verbose_name='Фамилия'
    )
    patronymic = models.CharField(
        max_length=20,
        null=True, blank=True,
        verbose_name='Отчество'
    )
    date_joined = models.DateTimeField(
        verbose_name="Дата регистрации",
        auto_now_add=True
    )
    last_login = models.DateTimeField(
        verbose_name="Дата последнего действия на сайте",
        auto_now=True
    )
    is_active = models.BooleanField(
        verbose_name="Активный?", default=True
    )
    is_admin = models.BooleanField(
        verbose_name="Админ?", default=False
    )
    is_superuser = models.BooleanField(
        verbose_name="Суперпользователь?", default=False
    )
    is_staff = models.BooleanField(
        verbose_name="Персонал?", default=False
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'email']
    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    def __str__(self):
        return self.username
