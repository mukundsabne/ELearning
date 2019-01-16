from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import Registration

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

def savestudent(request):
    fullname = request.POST['fullname']
    appliedfor = request.POST['appliedfor']
    dob = request.POST['dob']
    gender= request.POST['gender']
    contact1 = request.POST['mob1']
    contact2 = request.POST['mob2']
    district = request.POST['district']
    address = request.POST['address']
    apppliedprogram = request.POST['apppliedprogram']
    durationofprogram = request.POST['durationofprogram']
    durstionofmonth = request.POST['durstionofmonth']
    r = Registration(fullname=fullname,appliedfor=appliedfor,dob=dob,gender=gender,contact1=contact1,contact2=contact2,district=district,address=address,apppliedprogram=apppliedprogram,durationofprogram=durationofprogram,durstionofmonth=durstionofmonth)
    try:
        if request.method == 'POST':
            r.save()
            return redirect('reg')
        else:
            return render(request,'404.html',{'initial':'r'})

    except:
        return render(request,'404.html',{'initial':'r'})
