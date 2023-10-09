from django.forms import Form, CharField, TextInput, PasswordInput, EmailInput


class LoginForm(Form):
    username = CharField(label='Username', widget=TextInput(attrs={
        'id': 'username'
    }))
    password = CharField(label='Password', widget=PasswordInput(attrs={
        'id': 'password'
    }))


class RegisterForm(Form):
    first_name = CharField(label='First name', widget=TextInput(attrs={
        'id': 'first_name'
    }))
    last_name = CharField(label='Last name', widget=TextInput(attrs={
        'id': 'last_name'
    }))
    email = CharField(label='Email', widget=EmailInput(attrs={
        'id': 'email'
    }))
    username = CharField(label='Username', widget=TextInput(attrs={
        'id': 'username'
    }))
    password = CharField(label='Password', widget=PasswordInput(attrs={
        'id': 'password'
    }))
    confirm_password = CharField(label='Confirm password', widget=PasswordInput(attrs={
        'id': 'confirm_password'
    }))
