from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = "users"

urlpatterns = [

    path('register/', register, name= 'register'), 

    path('login/', LoginView.as_view(template_name = 'users/login.html'), name= 'login'),

    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name= 'logout'), 

    path('profile/', profile, name= 'profile'),

    path('profile/edit', edit_profile,  name='edit_profile'),

]
