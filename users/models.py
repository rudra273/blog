from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    first_name = models.CharField(max_length=20, blank = True, null = True) 

    last_name = models.CharField(max_length=20, blank = True, null = True)

    contact_number = models.CharField(max_length=20, default = '999999999') 

    image = models.ImageField(upload_to= 'profile_images/' , default= 'profile.jpg')

    bio = models.TextField(max_length = 500, blank = True, null = True) 

    def __str__(self) -> str:
        return self.user.username 



