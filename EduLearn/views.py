from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request,'index.html',{'initial':'h'})

def aboutus(request):
    send_mail('Automated Mail','Sending Mail From Elearning Website using billing software email....','Mukund',['vijaythakur015@gmail.com'])
    return render(request,'about-us.html',{'initial':'a'})

def services(request):
    return render(request,'services.html',{'initial':'s'})

def gallery(request):
    return render(request,'gallery.html',{'initial':'g'})

def contact(request):
    return render(request,'contact-us.html',{'initial':'c'})

def faq(request):
    return render(request,'faq.html',{'initial':'f'})

def reg(request):
    return render(request,'registration.html',{'initial':'r'})
