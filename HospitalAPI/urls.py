from django.conf.urls import url 
from HospitalAPI import views 
 
urlpatterns = [ 
    url(r'^api/patients$', views.patients_list),    #view all patients and their characteristics by cpf - first view
    url(r'^api/hospital/(?P<pk>[0-9]+)$', views.patients_detail),   #view chosen patient and characteristics by cpf - second view

    url(r'^api/cardiac$', views.cardiac_feed),    #to feed the database with the cardiac data
    url(r'^api/pulmonary$', views.pulmonary_feed),    #to feed the database with the pulmonary data
]