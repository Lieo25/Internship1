from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student



# Create your views here.
def home(request):
    return render(request,'home.html')
def index(request):
    data=Student.objects.all()
    print(data)

    return render(request,'index.html',{'data':data})

def add(request):
    if request.method=='POST':
        name=request.POST['name']
        rollno=request.POST['rollno']
        date=request.POST['date']
        one=request.POST['one']
        two=request.POST['two']
        three=request.POST['three']
        four=request.POST['four']
        five=request.POST['five']
        six=request.POST['six']
        seven=request.POST['seven']

        data=Student(name=name,rollno=rollno,date=date,one=one,two=two,three=three,four=four,five=five,six=six,seven=seven)
        data.save()
        if data:
            return redirect('/attendenceapp/index/')
    
    return render(request,'staff.html')

