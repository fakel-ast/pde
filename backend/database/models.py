from peewee import DateTimeField, CharField, IntegerField, BooleanField, ForeignKeyField, ManyToManyField, \
    DeferredThroughModel, SmallIntegerField
from datetime import datetime

from backend import pw

TABLE_PREFIX = 'cl__'
CASCADE = 'CASCADE'
SET_NULL = 'SET NULL'


def make_table_name(model_class):
    """Генерация префиксов в именах таблиц"""
    model_name = model_class.__name__
    return '{}{}'.format(TABLE_PREFIX, model_name.lower())


OrderConfigurationThrough = DeferredThroughModel()
OrderAdditionalAttributesThrough = DeferredThroughModel()


class BaseModel(pw.Model):
    created = DateTimeField(default=datetime.utcnow)
    updated = DateTimeField(default=datetime.utcnow, null=True)

    def save(self, *args, **kwargs):
        self.updated = datetime.utcnow()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        table_function = make_table_name
