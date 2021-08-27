from os import name
from mark.models import Student
from django.shortcuts import redirect, render
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def addmark(request):
    if request.method=='POST':
        id=request.POST['idno']
        name=request.POST['name']
        m1=int(request.POST['m1'])
        m2=int(request.POST['m2'])
        m3=int(request.POST['m3'])
        a=((m3+m2+m1)/3)
        if(a>80):
            g='A'
        elif(a>60):
            g='B'
        elif(a>40):
            g='C'
        else:
            g='D'
        if(Student.objects.filter(idno=id).exists()):
            messages.info(request,"Student already exisits")
            return redirect('addmark')
        else:
            student=Student(idno=id,name=name,m1=m1,m2=m2,m3=m3,average=a,grade=g)
            student.save()
            messages.info(request,"Student is added")
            return redirect("addmark")
    else:    
        return render(request,'addmark.html')
    
def viewmark(request):
    if request.method=='POST':
        id=request.POST['id']
        student=Student.objects.filter(idno=id)
        return render(request,'viewmark.html',{'shows':0,'students':student})
    else:
        return render(request,'viewmark.html',{'shows':1})
        