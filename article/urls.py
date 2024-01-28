from django.urls import path
from .views import *

app_name = 'article'

urlpatterns = [
    path('', index , name= 'index'),

    path('article/<int:pk>/', single_article, name='single_article'),  
]

