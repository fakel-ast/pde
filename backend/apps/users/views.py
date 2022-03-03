import sys
import uuid
from datetime import datetime, timedelta

from flask import session
from flask_login import login_user
import jwt

from backend.base import MyMethodView, user_required


class CreateUserView(MyMethodView):
    decorators = [user_required]

    def post(self, *args, **kwargs):
        try:

            from backend.database.models import User
            if self.data.get('password') and self.data.get('username'):
                user = User()
                user.create_user(password=self.data.get('password'), username=self.data.get('username'))
                user.save()
                if user:
                    return {'errors': False, 'new_user_id': user.id}, 201
            return {'errors': True, 'message': 'Not valid data'}, 400
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return {'errors': True, 'message': f'{e} in {format(exc_tb.tb_lineno)}'}


class ChangedUserView(MyMethodView):
    decorators = [user_required]

    def post(self, *args, **kwargs):
        try:

            from backend.database.models import User
            user = User.select().where(User.id == self.data.get('id')).first()
            if user:
                changed_fields = []

                if not user.check_password(self.data.get('password')):
                    user.password = user.generate_password(self.data.get('password'))
                    changed_fields.append('password')

                if changed_fields:
                    user.save(only=changed_fields)
                return {'errors': False, 'changed_fields': changed_fields}
            return {'errors': True, 'message': 'Not valid data'}

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return {'errors': True, 'message': f'{e} in {format(exc_tb.tb_lineno)}'}


class LoginView(MyMethodView):

    def post(self, *args, **kwargs):
        try:

            from backend.database.models import User, RefreshToken
            from code_skill import app

            user = User.select().where(User.username == self.data.get('username', '')).first()
            if user and user.check_password(self.data.get('password', '')):
                login_user(user, remember=True)

                token = jwt.encode({
                    'username': user.username,
                    'user_id': user.id,
                    'iat': datetime.utcnow(),
                    'exp': datetime.utcnow() + timedelta(minutes=15)},
                    app.config.get('SECRET_KEY', ''),
                    algorithm="HS256"
                )
                # save refresh token in session
                refresh_token = uuid.uuid4()
                session['refresh_token'] = refresh_token
                # Save token in bd. Or replace if this user_id exists
                RefreshToken\
                    .insert(token=refresh_token, user_id=user.id)\
                    .on_conflict('replace')\
                    .execute()

                return {'errors': False, 'token': token}

            return {'errors': True, 'message': 'Not valid data'}, 400

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return {'errors': True, 'message': f'{e} in {format(exc_tb.tb_lineno)}'}


class GetCurrentUserView(MyMethodView):
    decorators = [user_required]

    def post(self, *args, **kwargs):
        try:
            pass

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return {'errors': True, 'message': f'{e} in {format(exc_tb.tb_lineno)}'}


class RefreshTokenView(MyMethodView):

    def post(self, *args, **kwargs):
        from backend.database.models import RefreshToken, User
        from code_skill import app

        try:
            # try get refresh token from session
            old_refresh_token = session.get('refresh_token')

            if old_refresh_token:
                refresh_token = RefreshToken.select(
                    RefreshToken.id,
                    User.id.alias('user_id'),
                    User.username.alias('user_name'),
                ).join(
                    User
                ).where(
                    RefreshToken.token == old_refresh_token
                ).dicts().first()

                if refresh_token:
                    new_refresh_token = uuid.uuid4()
                    token = jwt.encode({
                        'username': refresh_token.get('user_name'),
                        'user_id': refresh_token.get('user_id'),
                        'iat': datetime.utcnow(),
                        'exp': datetime.utcnow() + timedelta(minutes=15)},
                        app.config.get('SECRET_KEY', ''),
                        algorithm="HS256"
                    )
                    # update refresh token
                    RefreshToken.update(
                        token=new_refresh_token
                    ).where(
                        RefreshToken.id == refresh_token.get('id')
                    ).execute()

                    # save NEW refresh token in session
                    session['refresh_token'] = new_refresh_token
                    return {'errors': False, 'token': token}

            return {'errors': True, 'message': 'Invalid data'}, 404
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return {'errors': True, 'message': f'{e} in {format(exc_tb.tb_lineno)}'}


class CheckJWTTokenView(MyMethodView):
    decorators = [user_required]

    def post(self, *args, **kwargs):
        return {'errors': False}


class LogoutView(MyMethodView):

    def post(self, *args, **kwargs):
        session.pop('refresh_token')
        return {'errors': True}

    def get(self, *args, **kwargs):
        session.pop('refresh_token')
        return {'errors': True}
