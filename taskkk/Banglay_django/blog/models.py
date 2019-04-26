from django.db import models


class Blog_post(models.Model):
    title= models.CharField(max_length=100)
    author= models.CharField(max_length=50)
    publication_date=models.DateTimeField()
    description =models.TextField()
    photo=models.ImageField(upload_to='blog_iamge')


    def __str__(self):
        return self.title

