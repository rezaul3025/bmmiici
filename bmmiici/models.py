from django.db import models

class Doctor(models.Model):
    title = models.CharField(max_length=10)
    firstName = models.CharField(max_length=55)
    lastName = models.CharField(max_length=55)
    specializations = models.TextField()
    addrLine1 = models.CharField(max_length = 100)
    addrLine2 = models.CharField(max_length =100)
    postCode = models.CharField(max_length = 20)
    city = models.CharField(max_length = 100)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=120)
    website = models.TextField()
    #specializations = models.ManyToManyField(Specialization)

class Specialization(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='DoctorSpecialization')
    
class DoctorSpecialization(models.Model):
    doctor = models.ForeignKey(Doctor)
    specialization = models.ForeignKey(Specialization)
    
class Patient(models.Model):
    title = models.CharField(max_length=10)
    firstName = models.CharField(max_length=55)
    lastName = models.CharField(max_length=55)
    addrLine1 = models.CharField(max_length = 100)
    addrLine2 = models.CharField("", max_length =100)
    postCode = models.CharField("", max_length = 20)
    city = models.CharField(max_length = 100)
    mobile = models.CharField(max_length=20)
    email = models.CharField("", max_length=120)
    dob = models.DateField()


