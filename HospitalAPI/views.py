from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from HospitalAPI.models import Patients,PatientsCardiac,PatientsPulmonary
from HospitalAPI.serializers import PatientsSerializer,CardiacSerializer,PulmonarySerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def patients_list(request):
    #basic view created
    #still have to update this view with the patients characteristics
    if request.method == 'GET':
        patient = Patients.objects.all()
        patients_serializer = PatientsSerializer(patient, many=True)
        return JsonResponse(patients_serializer.data, safe=False)
    elif request.method == 'POST':
        patient_data = JSONParser().parse(request)
        patient_serializer = PatientsSerializer(data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse(patient_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    elif request.method == 'DELETE':
#        count = Patients.objects.all().delete()
#        return JsonResponse({'message': '{} Patients were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def patients_detail(request, pk):
    # find patient by pk (cpf)
    try: 
        patient = Patients.objects.get(pk=pk)
    except Patients.DoesNotExist: 
        return JsonResponse({'message': 'The patient does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        #still have to update this view with the patients characteristics
        patient_serializer = PatientsSerializer(patient) 
        return JsonResponse(patient_serializer.data)
    elif request.method == 'PUT': 
        patient_data = JSONParser().parse(request) 
        patient_serializer = PatientsSerializer(patient, data=patient_data) 
        if patient_serializer.is_valid(): 
            patient_serializer.save() 
            return JsonResponse(patient_serializer.data) 
        return JsonResponse(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        patient.delete() 
        return JsonResponse({'message': 'Patient was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def cardiac_feed(request):
    cardiac_data = JSONParser().parse(request)
    cardiac_serializer = CardiacSerializer(data=cardiac_data)
    if cardiac_serializer.is_valid():
        cardiac_serializer.save()
        return JsonResponse(cardiac_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(cardiac_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def pulmonary_feed(request):
    pulmonary_data = JSONParser().parse(request)
    pulmonary_serializer = PulmonarySerializer(data=pulmonary_data)
    if pulmonary_serializer.is_valid():
        pulmonary_serializer.save()
        return JsonResponse(pulmonary_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(pulmonary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
