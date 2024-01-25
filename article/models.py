from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length = 2000) 

    def __str__(self) -> str:
        return self.title
    
    