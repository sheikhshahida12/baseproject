from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=200)
    roll=models.IntegerField(max_length=200)
    subject=models.CharField(max_length=200)

    def __str__(self):
        return self.name

    # Create your models here.
class employee(models.Model):

    name=models.CharField(max_length=200)
    id=models.IntegerField(primary_key=True)
    gender=models.CharField(max_length=200)
    salary=models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField(max_length=200)
    subject=models.CharField(max_length=200)

    def __str__(self):
        return self.name
