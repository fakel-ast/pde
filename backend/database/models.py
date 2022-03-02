from peewee import DateTimeField, CharField, IntegerField, BooleanField, ForeignKeyField, SmallIntegerField, TextField
from datetime import datetime

from backend import pw

TABLE_PREFIX = 'cl__'
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


class Task(BaseModel):
    """Model for task"""
    title = CharField(max_length=128, verbose_name='Название категории')
    point_count = SmallIntegerField(default=0, verbose_name='Количество очков за решение')
    description = TextField(null=True, verbose_name='Описание')

    class Meta:
        table_name = TABLE_PREFIX + 'task'
