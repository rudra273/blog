from django.urls import path
from .views import *

app_name = 'article'

urlpatterns = [
    
    path('', index , name= 'index'),

    path('article/<int:pk>/', single_article, name='single_article'), 

    path('article/category/<int:pk>/', categorised_article, name='categorised_article'),  

<<<<<<< HEAD
    path('article/post/', post_article, name= 'post_article'), 
=======
    path('article/create/', create_article, name='create_article'), 
>>>>>>> cdb048b7b40a3de253e08f3d3939f3d8960154e5

    
]

