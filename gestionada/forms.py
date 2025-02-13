from django import forms


class loginform(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class EditUserForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=100, required=False)


class EditDauserForm(forms.Form):
    subdelegacion = forms.CharField(max_length=100, required=True)
