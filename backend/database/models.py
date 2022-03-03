from peewee import DateTimeField, CharField, IntegerField, BooleanField, ForeignKeyField, SmallIntegerField, TextField
from datetime import datetime

from backend import pw
from backend.apps.users.mixins import CustomUserMixin

TABLE_PREFIX = 'cs__'
CASCADE = 'CASCADE'
SET_NULL = 'SET NULL'


def make_table_name(model_class):
    """Генерация префиксов в именах таблиц"""
    model_name = model_class.__name__
    return '{}{}'.format(TABLE_PREFIX, model_name.lower())


class BaseModel(pw.Model):
    created = DateTimeField(default=datetime.utcnow)
    updated = DateTimeField(default=datetime.utcnow, null=True)

    def save(self, *args, **kwargs):
        self.updated = datetime.utcnow()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        table_function = make_table_name


class TaskCategory(BaseModel):
    """Model for task category"""
    title = CharField(max_length=128, verbose_name='Название категории')
    image = CharField(null=True, verbose_name='Фото категории (svg)')
    active = BooleanField(default=True, verbose_name='Показывать категорию')

    class Meta:
        table_name = TABLE_PREFIX + 'task_category'


class TaskType(BaseModel):
    """Model for task type (simple text, program code)"""
    title = CharField(max_length=32, verbose_name='Название типа задачи')

    class Meta:
        table_name = TABLE_PREFIX + 'task_type'


class Task(BaseModel):
    """Model for task"""
    title = CharField(max_length=128, verbose_name='Название категории')
    point_count = SmallIntegerField(default=0, verbose_name='Количество очков за решение')
    description = TextField(null=True, verbose_name='Описание')
    type = ForeignKeyField(TaskType, verbose_name='Тип задачи')

    class Meta:
        table_name = TABLE_PREFIX + 'task'


class TaskAnswer(BaseModel):
    """Model for save user answer on task"""
    task = ForeignKeyField(Task, on_delete=CASCADE)
    answer = TextField(null=True, verbose_name='Текст ответа')
    is_success = BooleanField(default=False, verbose_name='Является ли ответ правильным')

    class Meta:
        table_name = TABLE_PREFIX + 'task_answer'


class TaskFile(BaseModel):
    """Model for attach files to task"""
    task = ForeignKeyField(Task, on_delete=CASCADE)
    file = CharField(max_length=128, verbose_name='Файл (название)')

    class Meta:
        table_name = TABLE_PREFIX + 'task_file'


class TaskHint(BaseModel):
    """Model for attach hint to task"""
    task = ForeignKeyField(Task, on_delete=CASCADE)
    hint = CharField(max_length=256, verbose_name='Текст подсказки')

    class Meta:
        table_name = TABLE_PREFIX + 'task_hint'


class Group(BaseModel):
    short_title = CharField(max_length=20, verbose_name='Короткое название группы', help_text='Например "ОИБ-418"')
    full_title = CharField(max_length=128, verbose_name='Полное название группы', null=True)

    class Meta:
        table_name = TABLE_PREFIX + 'group'


class User(BaseModel, CustomUserMixin):
    username = CharField(25, verbose_name='Логин')
    fio = CharField(256, verbose_name='ФИО пользователя', null=True)
    email = CharField(max_length=256, verbose_name='Email')
    password = CharField(256, verbose_name='Пароль')
    errors = IntegerField(
        default=0, verbose_name='Количество ошибок авторизации', help_text='Количество ошибок авторизации'
    )
    is_blocked = BooleanField(default=False, verbose_name='Флаг блокировки пользоваетля', null=True)
    group = ForeignKeyField(Group, verbose_name='Группа студента', null=True, on_delete=CASCADE)
    is_teacher = BooleanField(default=False, verbose_name='Является преподавателем')
    avatar = CharField(max_length=64, verbose_name='Аватар пользователя', null=True)
    online = BooleanField(default=False, verbose_name='Статус онлайн')
    last = DateTimeField(null=True, verbose_name='Дата последнего входа', default=None)

    class Meta:
        table_name = TABLE_PREFIX + 'user'


class UserSolvedTask(BaseModel):
    user = ForeignKeyField(User, on_delete=CASCADE)
    task = ForeignKeyField(Task, on_delete=CASCADE)

    class Meta:
        table_name = TABLE_PREFIX + 'user_solved_task'


class RefreshToken(BaseModel):
    """Refresh tokens"""
    token = CharField(max_length=64, verbose_name='refresh token')
    user = ForeignKeyField(User, on_delete='CASCADE', unique=True)

    class Meta:
        table_name = TABLE_PREFIX + 'refresh_token'
