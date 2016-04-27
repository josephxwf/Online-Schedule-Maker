from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
#from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
'''
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
'''
class registerForm(UserCreationForm):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    class Meta:
        model = User
        fields =('username','password')
    def save(self,commit=True):
        user = super(UserCreationForm,self).save(commit =False)
        user.password = self.cleaned_data['password']
        if commit:
            user.save()
        return user
