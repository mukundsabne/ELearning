from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/',views.aboutus,name='about'),
    path('services/',views.services,name='services'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/',views.contact,name='contact'),
    path('faq/',views.faq,name='faq'),
]
