from django.db import models

class Pacients(models.Model):
    pacientCPF = models.AutoField(primary_key=True)
    pacientName = models.CharField(max_length=100)
    pacientAge = models.IntegerField()
    pacientRG = models.CharField(max_length=20)
    pacientBirth = models.DateField()
    pacientSex = models.CharField(max_length=20)
    pacientSign = models.CharField(max_length=50)
    pacientMom = models.CharField(max_length=100)
    pacientFather = models.CharField(max_length=100)
    pacientEmail = models.CharField(max_length=100)
    pacientsPassword = models.CharField(max_length=100)
    pacientCep = models.CharField(max_length=10)
    pacientAdress = models.CharField(max_length=100)
    pacientAdressNumber = models.IntegerField()
    pacientAdressNeighborhood = models.CharField(max_length=100)
    pacientCity = models.CharField(max_length=100)
    pacientState = models.CharField(max_length=100)
    pacientHPhone = models.CharField(max_length=20)
    pacientPhone = models.CharField(max_length=20)
    pacientHeight = models.CharField(max_length=20)
    pacientWeight = models.IntegerField()
    pacientBlood = models.CharField(max_length=10)
    pacientColor = models.CharField(max_length=20)

class PacientsCardiac(models.Model):
    pacientCPF = models.AutoField(primary_key=True)
    pacientDate = models.CharField(max_length=10)
    pacientCEPOC = models.CharField(max_length=100)
    pacientInd_card = models.FloatField()

class PacientsPulmonary(models.Model):
    pacientCPF = models.AutoField(primary_key=True)
    pacientDate = models.CharField(max_length=10)
    pacientPEPOC = models.CharField(max_length=100)
    pacientInd_pulm = models.FloatField()