from django.db import models

# Create your models here.

class Registration(models.Model):
    fullname = models.CharField(max_length=200)
    appliedfor = models.CharField(max_length=200)
    dob = models.DateField()
    gender=models.CharField(max_length=200)
    contact1 = models.BigIntegerField(default=0)
    contact2 = models.BigIntegerField(default=0)
    district = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    apppliedprogram = models.CharField(max_length=200)
    durationofprogram = models.CharField(max_length=100)
    durstionofmonth = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname

class Demo(models.Model):
    fname = models.CharField(max_length=200)
    lname=models.CharField(max_length=200)

    def __str__(self):
        return self.fname+' '+self.lname

class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobileno = models.BigIntegerField(default=0)
    message = models.CharField(max_length=200)
