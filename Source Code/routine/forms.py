from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User
from .models import Computer_First,Computer_Second,Computer_Third,Computer_Fourth, Electrical_First, Electrical_Second, Electrical_Third, Electrical_Fourth, Labroom


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs = {'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class Computer1ModelForm(forms.ModelForm):
    class Meta:
        model = Computer_First
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']

class Computer2ModelForm(forms.ModelForm):
    class Meta:
        model = Computer_Second
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']

class Computer3ModelForm(forms.ModelForm):
    class Meta:
        model = Computer_Third
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']

class Computer4ModelForm(forms.ModelForm):
    class Meta:
        model = Computer_Fourth
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']


class Electrical1ModelForm(forms.ModelForm):
    class Meta:
        model = Electrical_First
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']

class Electrical2ModelForm(forms.ModelForm):
    class Meta:
        model = Electrical_Second
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']

class Electrical3ModelForm(forms.ModelForm):
    class Meta:
        model = Electrical_Third
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']

class Electrical4ModelForm(forms.ModelForm):
    class Meta:
        model = Electrical_Fourth
        fields = ['batch','semester','Lecturer_Name','Lecturer_Code',
                   'Lecturer_Id', 'Lecturer_Subject', 'Lecturer_Period',
                   'Lab_Class','Lab_Subject','Lab_Lec_Period']    

class LabroomModelForm(forms.ModelForm):
    class Meta:
        model = Labroom
        fields = ['Lab_Name', 'Lab_No']