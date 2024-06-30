from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Student
def index(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        studentid=request.POST.get('studentid')
        email=request.POST.get('email')
        college=request.POST.get('college')
        Dept=request.POST.get('Dept')
        Year=request.POST.get('Year')
        gender=request.POST.get('gender')
        print(name,studentid,email,college,Dept,Year,gender)

        data=Student(name=name,studentid=studentid,email=email,college=college,Dept=Dept,Year=Year,gender=gender)
        data.save()
        return redirect('newpage/')
    return render(request, 'form2.html')
def newpage(request):
    return render(request, 'newpage.html')
