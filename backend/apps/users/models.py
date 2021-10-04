from django.db import models
from django.contrib.auth.models import AbstractUser


class Group(models.Model):
    short_title = models.CharField(
        max_length=20, verbose_name='Короткое название группы',
        help_text='Например "ОИБ-418"')
    full_title = models.CharField(max_length=128, verbose_name='Полное название группы', null=True, blank=True)


class User(AbstractUser):
    group = models.ForeignKey(
        Group, verbose_name='Группа студента', null=True,
        blank=True, on_delete=models.CASCADE, related_name='students'
    )
    fio = models.CharField(max_length=128, verbose_name='ФИО пользователя')
    is_teacher = models.BooleanField(default=False, verbose_name='Является преподавателем')




