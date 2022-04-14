from rest_framework import serializers 
from HospitalAPI.models import Patients,PatientsCardiac,PatientsPulmonary

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patients
        fields=(
            'patientCPF',
            'patientName',
            'patientAge',
            'patientRG',
            'patientBirth',
            'patientSex',
            'patientSign',
            'patientMom',
            'patientFather',
            'patientEmail',
            'patientsPassword',
            'patientCep',
            'patientAdress',
            'patientAdressNumber',
            'patientAdressNeighborhood',
            'patientCity',
            'patientState',
            'patientHPhone',
            'patientPhone',
            'patientHeight',
            'patientWeight',
            'patientBlood',
            'patientColor')

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