from django import forms 
from django.forms import ModelForm 

from .models import Article


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = "__all__" 

        widgets ={
            # 'category' : forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'rows':'8', 'cols':'10','class':'form-control'}),  
        }

