from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Withdraw


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):

        model   = CustomUser
        fields  = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:

        model = CustomUser
        fields = UserChangeForm.Meta.fields



class SettingsForm(forms.ModelForm):

    class Meta:

        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'details',
            'profile_picture',
        ]


class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = [
            "withdraw_amount",
            "withdraw_method",
            "account_number"
        ]