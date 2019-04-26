from django.db import models



class Catagory(models.Model):
    name=models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    def __str__(self):
        return self.name


        
class Blog_Post(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    athor=models.CharField(max_length=100) 
    publication_date=models.DateTimeField()
    photo=models.ImageField()
    price=models.IntegerField()
    description =models.TextField()

    def __str__(self):
        return self.name