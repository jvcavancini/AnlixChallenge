from django.db import models

#change cpf to key
#working as an id now
class Patients(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    rg = models.CharField(max_length=20)
    data_nasc = models.DateField()
    sexo = models.CharField(max_length=20)
    signo = models.CharField(max_length=50)
    mae = models.CharField(max_length=100)
    pai = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    telefone_fixo = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    altura = models.CharField(max_length=20)
    peso = models.IntegerField()
    tipo_sanguineo = models.CharField(max_length=10)
    cor = models.CharField(max_length=20)

class PatientsCardiac(models.Model):
    patientCPF = models.ForeignKey(Patients,to_field="cpf", db_column="patientCPF", on_delete=models.CASCADE)
    patientDate = models.DateField()
    patientCEPOC = models.CharField(max_length=100)
    patientInd_card = models.FloatField()

class PatientsPulmonary(models.Model):
    patientCPF = models.ForeignKey(Patients,to_field="cpf", db_column="patientCPF", on_delete=models.CASCADE)
    patientDate = models.DateField()
    patientPEPOC = models.CharField(max_length=100)
    patientInd_pulm = models.FloatField()