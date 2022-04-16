from django.forms import DateTimeField
from rest_framework import serializers 
from HospitalAPI.models import Patients,PatientsCardiac,PatientsPulmonary

class PatientsSerializer(serializers.ModelSerializer):
    data_nasc=serializers.DateField(format="%d-%m-%Y", input_formats=['%d/%m/%Y', 'iso-8601'])
    
    class Meta:
        model=Patients
        fields=(
            'cpf',
            'nome',
            'idade',
            'rg',
            'data_nasc',
            'sexo',
            'signo',
            'mae',
            'pai',
            'email',
            'senha',
            'cep',
            'endereco',
            'numero',
            'bairro',
            'cidade',
            'estado',
            'telefone_fixo',
            'celular',
            'altura',
            'peso',
            'tipo_sanguineo',
            'cor')

class CardiacSerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientsCardiac
        fields=(
            'patientCPF',
            'patientDate',
            'patientCEPOC',
            'patientInd_card')

class PulmonarySerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientsPulmonary
        fields=(
            'patientCPF',
            'patientDate',
            'patientPEPOC',
            'patientInd_pulm')