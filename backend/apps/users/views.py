import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.generic import FormView, TemplateView

from apps.users.forms import MyUserCreationForm


class SignUpView(FormView):
    form_class = MyUserCreationForm
    template_name = ''

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        if user:
            login(self.request, user)
            return JsonResponse({'errors': False, 'new_user_id': user.id})
        else:
            return JsonResponse({'errors': False, 'message': 'Ну тут мои полномочия все.'})

    def get_form(self, form_class=None):
        return self.form_class(json.loads(self.request.body.decode('utf-8')))

    def form_invalid(self, form):
        return_dict = {}
        errors = form.errors.get_json_data()

        # if error for all fields, show it how message
        if errors.get('__all__', [{}])[0].get('message', ''):
            return_dict['messages'] = [errors.get('__all__', [{}])[0].get('message', '')]
            del errors['__all__']
        # if was errors for field (not __all__), save as dict
        if errors:
            return_dict['errors_dict'] = errors
        return JsonResponse({'errors': True, **return_dict})


class SignInView(TemplateView):
    template_name = ''

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode('utf-8'))

        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return JsonResponse({'errors': False, 'username': user.username})
        else:
            return JsonResponse({'errors': True, 'messages': ['Неправильный логин или пароль']})


class LogoutView(TemplateView):

    def post(self, *args, **kwargs):
        logout(self.request)
        return JsonResponse({'errors': False, 'messages': ['Вы успешно вышли из аккаунта']})

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
