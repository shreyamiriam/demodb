from django.shortcuts import render
from .models import employee
# Create your views here.
def index(request):
    return render(request,'index.html')

def addperson(request):
    responsedic={}
    try:
        Name=request.POST['name']
        Address=request.POST['address']
        emplist=employee(name=Name,address=Address)
        emplist.save()
        responsedic["msg"]="Employee added"
        return render(request,'index.html',responsedic)
    except Exception as e:
        print(e)
        responsedic['msg']="Employee cannot be added"
        return render(request,'index.html',responsedic)
    
def disp(request):
    empdtls=employee.objects.all()
    return render(request,'index.html',{'emp':empdtls})

def delete(request):
    Name=request.POST['name']
    empdtls=employee.objects.filter(name=Name)
    empdtls.delete()
    return render(request,'index.html',{'msg1':"Record deleted"})