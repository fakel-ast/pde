from django.contrib.auth import get_user_model
from django.db import models


class TaskCategory(models.Model):
    """Категории задач"""
    title = models.CharField(max_length=128, verbose_name='Название категории')
    description = models.CharField(
        max_length=1024, verbose_name='Краткое описание задач, которые будут в данной категории'
    )
    image = models.ImageField(upload_to='tasks/category', null=True, blank=True, verbose_name='Фото категории')
    active = models.BooleanField(default=True, verbose_name='Показывать категорию')


class Task(models.Model):
    """Задачи"""
    title = models.CharField(max_length=128, verbose_name='Название задачи')
    author = models.ForeignKey(
        get_user_model(), null=True, blank=True, verbose_name='Автор',
        on_delete=models.SET_NULL, related_name='tasks'
    )
    category = models.ForeignKey(TaskCategory, verbose_name='Категория', on_delete=models.CASCADE, related_name='tasks')
    text = models.TextField(verbose_name='Текст задачи', null=True, blank=True)
    answer = models.CharField(max_length=1024, verbose_name='Правильный ответ')
    answer_format = models.CharField(max_length=20, verbose_name='Формат ответа')
    help_text = models.CharField(max_length=1024, verbose_name='Подсказка', null=True, blank=True)
    points = models.PositiveIntegerField(verbose_name='Очки за задачу')
    taken_from_site = models.CharField(
        max_length=128, verbose_name='С какого сайта была взята задача',
        null=True, blank=True
    )
    active = models.BooleanField(default=True, verbose_name='Показывать задачу')
    solved_users = models.ManyToManyField(get_user_model(), verbose_name='Решившие пользователи', blank=True)


class Files(models.Model):
    """Прикрепленные к задачам файлы"""
    file = models.FileField(upload_to='tasks/files', verbose_name='Файл', null=True)
    task = models.ForeignKey(Task, verbose_name='Задача', on_delete=models.CASCADE)
