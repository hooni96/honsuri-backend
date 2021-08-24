from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

# 관리자페이지에서 사용하는 폼 수정. 우리 커스텀 유저에 맞는 폼을 생성.
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'name', 'nickname', 'phone_number', 'alcohol_amount', 'favorite_alcohol', 'favorite_food', 'favorite_combination',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'name', 'nickname', 'phone_number', 'alcohol_amount', 'favorite_alcohol', 'favorite_food', 'favorite_combination', 'is_active', 'is_admin',)

    def clean_password(self):
        return self.initial["password"]