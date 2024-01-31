from django import forms 
from django.forms import ModelForm 

from .models import Article

<<<<<<< HEAD

=======
>>>>>>> cdb048b7b40a3de253e08f3d3939f3d8960154e5
class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
<<<<<<< HEAD
        fields = "__all__" 

        widgets ={
            # 'category' : forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'rows':'8', 'cols':'10','class':'form-control'}),  
        }

=======
        fields = "__all__"  
>>>>>>> cdb048b7b40a3de253e08f3d3939f3d8960154e5
