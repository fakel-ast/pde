from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from flask_login import AnonymousUserMixin, UserMixin


class CustomAnonymousUserMixin(AnonymousUserMixin):

    def has_roles(self, *args, **kwargs):
        return False

    @property
    def id(self, *args, **kwargs):
        return 0

    @id.setter
    def id(self, *args, **kwargs):
        return


class CustomUserMixin(UserMixin):

    def has_roles(self, *args, **kwargs):
        roles_for_checking = [*args]
        return False

    @property
    def is_superuser(self, *args, **kwargs):
        return self.has_roles('admin')

    @staticmethod
    def generate_password(password):
        """Установка нового пароля"""
        return generate_password_hash(password)

    def check_password(self, password):
        """Сравнение пароля"""
        return check_password_hash(self.password, password)

    def create_user(self, password: str, username: str, fio: str = '', email: str = ''):
        self.password = self.generate_password(password)
        self.username = username
        self.fio = fio
        self.email = email

    def is_blocked(self):
        """проверка блокировки пользователя"""
        print(self.blocked)
        if self.blocked:
            if self.blocked > datetime.utcnow():
                return True
            self.blocked = None
            self.save(only=['blocked', 'updated'])
        return False