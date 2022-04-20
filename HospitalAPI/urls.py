from django.urls import re_path, path
from HospitalAPI import views 
 
urlpatterns = [ 
    re_path(r'api/patients', views.patients_list),    #view all patients and their characteristics by cpf - first view
    re_path(r'api/(?P<pk>[0-9]+)$', views.patients_detail),   #view chosen patient and characteristics by cpf - second view
    re_path(r'api/date/(?P<kdate>[0-9]+)$', views.dates_detail),
    re_path(r'api/rangedate/(?P<startdate>[0-9]+)/(?P<enddate>[0-9]+)$', views.datesrange_detail),
    re_path(r'api/valuerange/(?P<pk>[0-9]+)/(?P<startvalue>[0-9]+)/(?P<endvalue>[0-9]+)$', views.valuerange),
    re_path(r'api/namesearch/(?P<name>[\w]+)$', views.patients_name),

    re_path('api/cardiac', views.cardiac_feed),    #to feed the database with the cardiac data
    re_path('api/pulmonary', views.pulmonary_feed),    #to feed the database with the pulmonary data
]