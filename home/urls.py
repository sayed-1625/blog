from django.urls import path
from home.views import index, descripcion, miDoctorYa

urlpatterns = [
    path('index/', index, name='index'),
    path('gmys/', descripcion, name='gmys'),
    path('miDoctorYa/', miDoctorYa, name='miDoctorYa'),
]
