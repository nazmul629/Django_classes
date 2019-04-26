from django.db import models

class Catagory(models.Model):
    name=models.CharField(max_length=100)
    is_active = models.BooleanField()


    def __str__(self):
        return self.name


        
class BlogPost(models.Model):
    category= models.ForeignKey(Catagory,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    athor=models.CharField(max_length=100) 
    publication_date=models.DateTimeField()
    photo=models.ImageField()
    description =models.TextField()
    is_published = models.BooleanField()

    def __str__(self):
        return self.title



class Book(models.Model):
    name = models.CharField(max_length = 50)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    name = models.CharField(max_length=50)
    acc_no = models.CharField(max_length=50)
    balance = models.IntegerField()

    def __str__(self):
        return self.name

