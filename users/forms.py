from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from users.models import Userc


class ProfileCreateChange(ModelForm):
    """form for profile"""
    class Meta:
        model = Userc
        fields = {'username', 'password', 'email', 'profile_img'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['.class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm, ModelForm):
    """form for logging in"""
    class Meta:
        model = Userc
        fields = {'username', 'password'}