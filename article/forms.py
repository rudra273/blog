from django import forms 
from django.forms import ModelForm 
from .models import Article

class BootstrapImageWidget(forms.ClearableFileInput):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'form-control'} 
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs) 

class ArticleForm(forms.ModelForm):

    img = forms.ImageField(label='Upload a image', widget=BootstrapImageWidget())
    class Meta:
        model = Article
        fields = "__all__" 

        widgets ={
            'category' : forms.Select(attrs={'class': 'form-select'}),

            'title': forms.TextInput(attrs={'class': 'form-control'}),

            'content': forms.Textarea(attrs={'rows':'8', 'cols':'10','class':'form-control'}), 
        } 



