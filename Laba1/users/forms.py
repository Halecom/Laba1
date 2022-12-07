from django import forms
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    def clean_password(self):

        password = self.cleaned_data['password']

        for i in password:
            if not('A' <= i <= 'z' or '0' <= i <= '9'):
                raise ValidationError("Пароль может состоять только из латинских букв и цифр")
        return password
class ChangeForm(forms.Form):
    oldpassword = forms.CharField(label="Старый пароль", widget=forms.PasswordInput())
    newpassword = forms.CharField(label="Новый пароль", widget=forms.PasswordInput())
    acceptpassword = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput())
    def clean_newpassword(self):

        newpassword = self.cleaned_data['newpassword']

        for i in newpassword:
            if not('A' <= i <= 'z' or '0' <= i <= '9'):
                raise ValidationError("Пароль может состоять только из латинских букв и цифр")
        return newpassword

