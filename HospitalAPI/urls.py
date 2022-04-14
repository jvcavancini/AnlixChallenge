from django.urls import re_path, path
from HospitalAPI import views 
 
urlpatterns = [ 
    #path('ab', views.patients_list),    #view all patients and their characteristics by cpf - first view
    re_path(r'api/patients', views.patients_list),    #view all patients and their characteristics by cpf - first view
    re_path(r'api/hospital/(?P<pk>[0-9]+)$', views.patients_detail),   #view chosen patient and characteristics by cpf - second view

    re_path('api/cardiac', views.cardiac_feed),    #to feed the database with the cardiac data
    re_path('api/pulmonary', views.pulmonary_feed),    #to feed the database with the pulmonary data
]