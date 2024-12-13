# Generated by Django 5.1.4 on 2024-12-12 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(blank=True, error_messages={'unique': 'Такой username ученика уже существует'}, max_length=20, null=True, unique=True, verbose_name='Логин')),
                ('email', models.CharField(blank=True, error_messages={'unique': 'Такой email ученика уже существует'}, max_length=30, null=True, unique=True, verbose_name='Почта')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=20, null=True, verbose_name='Отчество')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Дата последнего действия на сайте')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный?')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Админ?')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Суперпользователь?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Персонал?')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
