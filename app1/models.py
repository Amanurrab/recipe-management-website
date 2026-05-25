from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    image=models.ImageField()
    file=models.FileField()
  
    phone = models.CharField(max_length=15, null=True)  # NEW FIELD


class Product(models.Model):
    pass


class car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField(default=30)

    def __str__(self) -> str:
        return self.car_name
