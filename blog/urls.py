from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'), 


    path('', include('article.urls')),   
    path('users/', include('users.urls')), 

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
