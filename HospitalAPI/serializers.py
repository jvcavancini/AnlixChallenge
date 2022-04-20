from django.forms import DateTimeField
from rest_framework import serializers 
from HospitalAPI.models import Patients,PatientsCardiac,PatientsPulmonary

class CardiacSerializer(serializers.ModelSerializer):

    patientCPF=serializers.SlugRelatedField(
        queryset = Patients.objects.all(),
        slug_field='cpf'
    )

    class Meta:
        model=PatientsCardiac
        fields=(
            'patientCPF',
            'patientDate',
            'patientCEPOC',
            'patientInd_card')

    def create(self, validated_data):
        patient_cpf = validated_data.pop('patientCPF')
        #print(str(validated_data["patientCPF"]))
        patient = Patients.objects.get(cpf=patient_cpf)
        print(patient)
        patient_info = PatientsCardiac.objects.create(patientCPF = patient, **validated_data)
        return patient_info

class PulmonarySerializer(serializers.ModelSerializer):

    patientCPF=serializers.SlugRelatedField(
        queryset = Patients.objects.all(),
        slug_field='cpf'
    )

    class Meta:
        model=PatientsPulmonary
        fields=(
            'patientCPF',
            'patientDate',
            'patientPEPOC',
            'patientInd_pulm')

    def create(self, validated_data):
        patient_cpf = validated_data.pop('patientCPF')
        patient = Patients.objects.get(cpf=patient_cpf)
        patient_info = PatientsPulmonary.objects.create(patientCPF = patient, **validated_data)
        return patient_info

class PatientsSerializer(serializers.ModelSerializer):
    data_nasc = serializers.DateField(format="%d-%m-%Y", input_formats=['%d/%m/%Y', 'iso-8601'])
    cardiac = CardiacSerializer(many=True)
    pulmonary = PulmonarySerializer(many=True)
        
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
            'cor',
            'cardiac',
            'pulmonary')
