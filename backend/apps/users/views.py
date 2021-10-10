from django.contrib.auth import authenticate, login
from django.views.generic import FormView, TemplateView


class SignUpView(TemplateView):
    template_name = 'reg.html'

    def post(self, *args, **kwargs):
        print(self.request.POST)
        print(args)
        # print(form.cleaned_data)
        # form.save()
        # username = form.cleaned_data['username']
        # raw_password = form.cleaned_data['password1']
        # user = authenticate(username=username, password=raw_password)
        #
        # login(self.request, user)
