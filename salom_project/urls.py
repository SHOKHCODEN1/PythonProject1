from django.urls import path
from . import views
from .views import hamma_kitoblar , kitob_detail

urlpatterns = [
    path('', views.home, name='home'),
    path('salom/ber/', views.salom_ber, name='salom_ber'),
    path('mamlakat/', views.mamlakat, name='mamlakat'),
    path('mamlakat/viloyat/', views.mamlakat_viloyat, name='mamlakat_viloyat'),
    path('mamlakat/viloyat/shahar/', views.mamlakat_viloyat_shahar, name='mamlakat_viloyat_shahar'),
    path('mamlakat/viloyat/shahar/akademiya/', views.mamlakat_viloyat_shahar_akademiya, name='akademiya'),
    path('kitoblar/', hamma_kitoblar, name='hamma_kitoblar'),
    path('kitoblar/<int:id>/', kitob_detail , name='detail')
]