from django import forms
class UserRegistr(forms.Form):
    username = forms.CharField(max_length=30, label= 'Введите логин:')
    balance = forms.IntegerField(min_value=0, label='Введите баланс:')
    age = forms.IntegerField(min_value=18,max_value=103, label="Введите свой возраст:")