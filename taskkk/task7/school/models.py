from django.db import models

class StudentInfo(models.Model):
    Name=models.CharField(max_length=50)
    Roll= models.IntegerField()
    Result= models.IntegerField()
    District=models.CharField(max_length=50)
    Divition=models.CharField(max_length=50)

    def __str__(self):
        return self.Name