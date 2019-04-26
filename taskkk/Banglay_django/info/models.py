from django.db import models


class Profile(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField()
    photo=models.ImageField(upload_to='blog_iamge')
    eamil=models.EmailField()
    web=models.URLField()
    gender=models.CharField(max_length=10)

    def __str__(self):
            return self.name