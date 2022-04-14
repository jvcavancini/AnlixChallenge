from rest_framework import serializers 
from HospitalAPI.models import Pacients,PacientsCardiac,PacientsPulmonary

class PacientsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pacients
        fields=(
            'pacientCPF',
            'pacientName',
            'pacientAge',
            'pacientRG',
            'pacientBirth',
            'pacientSex',
            'pacientSign',
            'pacientMom',
            'pacientFather',
            'pacientEmail',
            'pacientsPassword',
            'pacientCep',
            'pacientAdress',
            'pacientAdressNumber',
            'pacientAdressNeighborhood',
            'pacientCity',
            'pacientState',
            'pacientHPhone',
            'pacientPhone',
            'pacientHeight',
            'pacientWeight',
            'pacientBlood',
            'pacientColor')

class CardiacSerializer(serializers.ModelSerializer):
    class Meta:
        model=PacientsCardiac
        fields=(
            'pacientCPF',
            'pacientDate',
            'pacientCEPOC',
            'pacientInd_card')

class PulmonarySerializer(serializers.ModelSerializer):
    class Meta:
        model=PacientsPulmonary
        fields=(
            'pacientCPF',
            'pacientDate',
            'pacientPEPOC',
            'pacientInd_pulm')