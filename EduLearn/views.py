from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import Registration,Contact
from django.http import HttpResponse
from django.core import serializers



def index(request):
    request.session['msg'] = None
    return render(request,'index.html',{'initial':'h'})

def aboutus(request):
    request.session['msg'] = None
    #send_mail('Automated Mail','Sending Mail From Elearning Website using billing software email....','Mukund',['vijaythakur015@gmail.com'])
    return render(request,'about-us.html',{'initial':'a'})

def services(request):
    request.session['msg'] = None
    return render(request,'services.html',{'initial':'s'})

def gallery(request):
    request.session['msg'] = None
    return render(request,'gallery.html',{'initial':'g'})

def contact(request):
    return render(request,'contact-us.html',{'initial':'c'})

def faq(request):
    request.session['msg'] = None
    return render(request,'faq.html',{'initial':'f'})

def reg(request):
    return render(request,'registration.html',{'initial':'r'})

def viewstudent(request):
    return render(request,'viewstudents.html')

def ajx(request):
    r = Registration.objects.all()
    data = serializers.serialize('json', r, fields=('fullname','id','appliedfor','dob','gender','contact1','contact2','district','address','apppliedprogram','durationofprogram','durstionofmonth'))
    return HttpResponse(data)


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
            request.session['msg'] = "Inserted Succesfully !!!"
            return redirect('reg')
        else:
            return render(request,'404.html',{'initial':'r'})

    except Exception as e:
        return render(request,'404.html',{'initial':'r','e':e})

def savecontact(request):
    fullname = request.POST['fullname']
    contact = request.POST['mob']
    email = request.POST['email']
    message = request.POST['msg']
    c = Contact(fullname=fullname,mobileno=contact,email=email,message=message)
    try:
        if request.method == 'POST':
            c.save()
            request.session['msg'] = "Thanks For Your Interest.. We Will Contact You Very Soon !!!"
            return redirect('contact')
        else:
            return render(request,'404.html',{'initial':'r'})

    except Exception as e:
        return render(request,'404.html',{'initial':'r','e':e})
