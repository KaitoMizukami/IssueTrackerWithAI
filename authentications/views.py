from django.shortcuts import render, redirect
from django.views.generic import FormView, View
from django.contrib.auth import authenticate, login, logout

from authentications.forms import UserLoginForm, UserCreationForm

# Create your views here.
class UserLoginView(FormView):
    template_name = 'authentications/login.html'
    form_class = UserLoginForm

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('teams:list')
        return redirect('authentications:login')
    

class UserSignupView(FormView):
    template_name = 'authentications/signup.html'
    form_class = UserCreationForm

    def post(self, request, *args, **kwargs):
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user = authenticate(email=user_form.cleaned_data['email'], password=user_form.cleaned_data['password'])
            login(request, user)
            return redirect('teams:list')
        else:
            return render(request, self.template_name, {'form': user_form})
        

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('authentications:login')