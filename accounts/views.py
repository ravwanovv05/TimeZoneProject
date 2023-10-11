from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.hashable import make_hashable
from django.views import View

from accounts.forms import RegisterForm

User = get_user_model()


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists!")
                return redirect('/accounts/register')
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
                return redirect('/accounts/register')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=confirm_password
                )
                user.save()
                return redirect('/login')
        else:
            messages.error(request, 'Passwords are not same!')
            return redirect('/register')


# def registration(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data.get('first_name')
#             last_name = form.cleaned_data.get('last_name')
#             email = form.cleaned_data.get('email')
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             confirm_password = form.cleaned_data.get('confirm_password')
#             if password == confirm_password:
#                 if User.objects.filter(email=email).exists():
#                     messages.error(request, "Email already exists!")
#                     return redirect('/accounts/register')
#                 if User.objects.filter(username=username).exists():
#                     messages.error(request, "Username already exists!")
#                     return redirect('/accounts/register')
#                 else:
#                     user = User.objects.create_user(
#                         first_name=first_name,
#                         last_name=last_name,
#                         email=email,
#                         username=username,
#                         password=confirm_password
#                     )
#                     user.save()
#                     return redirect('/accounts/login')
#             else:
#                 messages.error(request, 'Passwords are not same!')
#                 return redirect('/accounts/register')
#     else:
#         form = RegisterForm()
#     return render(request, "register.html", {'form': form})


class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        try:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, 'Invalid username or password!')
                    return redirect('login')
        except:
            return redirect('login')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')


