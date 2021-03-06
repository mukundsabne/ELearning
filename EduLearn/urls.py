from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/',views.aboutus,name='about'),
    path('services/',views.services,name='services'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/',views.contact,name='contact'),
    path('faq/',views.faq,name='faq'),
    path('reg/',views.reg,name='reg'),
    path('ajx/',views.ajx,name='ajx'),
    path('savestudent/',views.savestudent,name='savestudent'),
    path('savecontact/',views.savecontact,name='savecontact'),
    path('viewstudent/',views.viewstudent,name='viewstudent'),
]
