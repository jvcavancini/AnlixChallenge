from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
import datetime

from HospitalAPI.models import Patients,PatientsCardiac,PatientsPulmonary
from HospitalAPI.serializers import PatientsSerializer,CardiacSerializer,PulmonarySerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def patients_list(request):
    if request.method == 'GET':
        patients = Patients.objects.all()
        patients_serializer = PatientsSerializer(patients, many=True)
        return JsonResponse(patients_serializer.data, safe=False)
    if request.method == 'POST':
        patient_data = JSONParser().parse(request)
        patient_serializer = PatientsSerializer(data=patient_data, many=True)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse(patient_serializer.data, status=status.HTTP_201_CREATED, safe=False) 
        return JsonResponse(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
 
@api_view(['GET'])
def patients_detail(request, pk):
    try:
        pk=str(pk)
        pk=pk[0:3]+"."+pk[3:6]+"."+pk[6:9]+"-"+pk[9:11]
        patient = Patients.objects.get(cpf=pk)
    except Patients.DoesNotExist: 
        return JsonResponse({'message': 'The patient does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        patient_serializer = PatientsSerializer(patient)
        return JsonResponse(patient_serializer.data, safe=False)

@api_view(['GET'])
def dates_detail(request, kdate):
    try:
        kyear = int(kdate[0:4])
        kmonth = int(kdate[4:6])
        kday = int(kdate[6:8])
        patient = Patients.objects.filter(cardiac__patientDate=datetime.date(kyear, kmonth, kday)).distinct()
    except Patients.DoesNotExist: 
        return JsonResponse({'message': 'This date is unavailable'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        patient_serializer = PatientsSerializer(patient, many=True)
        return JsonResponse(patient_serializer.data, safe=False)

@api_view(['GET'])
def datesrange_detail(request, startdate, enddate):
    try:
        startdate = datetime.date(int(startdate[0:4]),int(startdate[4:6]),int(startdate[6:8]))
        enddate = datetime.date(int(enddate[0:4]),int(enddate[4:6]),int(enddate[6:8]))
        patient = Patients.objects.filter(cardiac__patientDate__range=(startdate,enddate)).distinct()
    except Patients.DoesNotExist:
        return JsonResponse({'message': 'This date is unavailable'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        patient_serializer = PatientsSerializer(patient, many=True)
        return JsonResponse(patient_serializer.data, safe=False)

@api_view(['GET'])
def valuerange(request, pk, startvalue, endvalue):
    try:
        pk=str(pk)
        pk=pk[0:3]+"."+pk[3:6]+"."+pk[6:9]+"-"+pk[9:11]
        startvalue=int(startvalue)/100
        endvalue=int(endvalue)/100
        patient = Patients.objects.filter(cpf=pk, cardiac__patientInd_card__range=(startvalue,endvalue), pulmonary__patientInd_pulm__range=(startvalue,endvalue)).distinct()
    except Patients.DoesNotExist:
        return JsonResponse({'message': 'This date is unavailable'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        patient_serializer = PatientsSerializer(patient, many=True)
        return JsonResponse(patient_serializer.data, safe=False)

@api_view(['GET'])
def patients_name(request, name):
    try:
        patient = Patients.objects.filter(nome__contains=name).distinct()
    except Patients.DoesNotExist:
        return JsonResponse({'message': 'This date is unavailable'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        patient_serializer = PatientsSerializer(patient, many=True)
        return JsonResponse(patient_serializer.data, safe=False)

@api_view(['POST'])
def cardiac_feed(request):
    cardiac_data = JSONParser().parse(request)
    cardiac_serializer = CardiacSerializer(data=cardiac_data, many=True)
    if cardiac_serializer.is_valid():
        cardiac_serializer.create(cardiac_serializer.data)
        return JsonResponse(cardiac_serializer.data, status=status.HTTP_201_CREATED, safe=False) 
    return JsonResponse(cardiac_serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

@api_view(['POST'])
def pulmonary_feed(request):
    pulmonary_data = JSONParser().parse(request)
    pulmonary_serializer = PulmonarySerializer(data=pulmonary_data, many=True)
    if pulmonary_serializer.is_valid():
        pulmonary_serializer.create(pulmonary_serializer.data)
        return JsonResponse(pulmonary_serializer.data, status=status.HTTP_201_CREATED, safe=False) 
    return JsonResponse(pulmonary_serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)