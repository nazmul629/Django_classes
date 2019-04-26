from django.db import models


class City(models.Model):
    Name = models.CharField(max_length=100)


    def __str__(self):
        return self.Name


class BiCategory(models.Model):
    Name = models.CharField(max_length=100)
    Icon = models.ImageField()


    def __str__(self):
        return self.Name


class Product(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    Description = models.TextField()
    Pub_date = models.DateTimeField()
    Photo = models.ImageField()
    Condition = models.TextField()
    Category = models.ForeignKey(BiCategory,on_delete=models.CASCADE)
    Location = models.ForeignKey(City,on_delete=models.CASCADE)


    def __str__(self):
        return self.Name


class BankAccount(models.Model):
    name = models.CharField(max_length=50)
    acc_no = models.CharField(max_length=50)
    balance = models.IntegerField()

    def __str__(self):
        return self.name