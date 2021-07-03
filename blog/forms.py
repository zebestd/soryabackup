from django import forms
from django.forms import ModelForm
from .models import *


class SoruForm(ModelForm):
    class Meta:
         model = Post
         fields = ('isim', 'soru', 'kategori', 'aciklama')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['isim', 'kimlik', 'yanit']