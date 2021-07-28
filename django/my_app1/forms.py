from django import forms
from django.core import validators
from django.forms import fields
from my_app1 import models


# class user_form(forms.Form):
#     userName = forms.CharField(label="User Name" , widget= forms.TextInput(attrs={
#         'placeholder' : 'Enter your full name' , 
#         'style': 'width:300px'
#     }))
#     email = forms.EmailField(label="User Email" , widget=forms.TextInput(attrs={
#         'placeholder' : 'Enter your email address'
#     }))
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirmPassword = forms.CharField(widget=forms.PasswordInput)
#     userDob = forms.DateField(label="Date Of Birth" , widget=forms.TextInput(attrs={
#         'type' : 'date'
#     }))

    
#     #to check if number is even or not
#     def even_or_not(value):
#         if value % 2 == 1:
#             raise forms.ValidationError("Plese Insert an Even Number")

#     evenNumber = forms.IntegerField(label="enter an even number" , validators=[even_or_not])



    # to check two inputs value ar same
    # def clean(self):
    #     all_cleaned_data =  super().clean()

    #     password = all_cleaned_data['password']

    #     confirmPassword = all_cleaned_data['confirmPassword']

    #     if password != confirmPassword:
    #         raise forms.ValidationError("Password Doesn't match!")


class MusicianForm(forms.ModelForm):
    class Meta:
        model  = models.Musician
        fields = "__all__"


class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type' : 'date'}))
    class Meta: 
        model = models.Album
        fields = "__all__"
        