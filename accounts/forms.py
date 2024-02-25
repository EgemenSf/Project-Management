from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"placeholder": "Username or email"}))
    password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"}))


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"placeholder": "Choose your username"}))
    password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={"placeholder": "Choose your password"}))
    password_confirmation = forms.CharField(
        max_length=150, widget=forms.PasswordInput(attrs={"placeholder": "Enter your password again"})
    )
