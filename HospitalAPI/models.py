from django.db import models

class Patients(models.Model):
    patientCPF = models.AutoField(primary_key=True)
    patientName = models.CharField(max_length=100)
    patientAge = models.IntegerField()
    patientRG = models.CharField(max_length=20)
    patientBirth = models.DateField()
    patientSex = models.CharField(max_length=20)
    patientSign = models.CharField(max_length=50)
    patientMom = models.CharField(max_length=100)
    patientFather = models.CharField(max_length=100)
    patientEmail = models.CharField(max_length=100)
    patientsPassword = models.CharField(max_length=100)
    patientCep = models.CharField(max_length=10)
    patientAdress = models.CharField(max_length=100)
    patientAdressNumber = models.IntegerField()
    patientAdressNeighborhood = models.CharField(max_length=100)
    patientCity = models.CharField(max_length=100)
    patientState = models.CharField(max_length=100)
    patientHPhone = models.CharField(max_length=20)
    patientPhone = models.CharField(max_length=20)
    patientHeight = models.CharField(max_length=20)
    patientWeight = models.IntegerField()
    patientBlood = models.CharField(max_length=10)
    patientColor = models.CharField(max_length=20)

class PatientsCardiac(models.Model):
    patientCPF = models.AutoField(primary_key=True)
    patientDate = models.CharField(max_length=10)
    patientCEPOC = models.CharField(max_length=100)
    patientInd_card = models.FloatField()

class PatientsPulmonary(models.Model):
    patientCPF = models.AutoField(primary_key=True)
    patientDate = models.CharField(max_length=10)
    patientPEPOC = models.CharField(max_length=100)
    patientInd_pulm = models.FloatField()