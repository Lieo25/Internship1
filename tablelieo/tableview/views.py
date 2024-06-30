from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from tableview.models import Tableview


# Create your views here.
def index(request):
    data=Tableview.objects.all()
    if request.method == 'POST':
        name = request.POST.get('fname')
        email = request.POST.get('lname')
        print(name, email)
        obj=Tableview(name=name, email=email)
        obj.save()
        
    return render(request, 'table.html',{'data':data})

def delete(request, id):
    mem=Tableview.objects.get(id=id)
    mem.delete()
    return redirect("/table")


def update(request, id):
    update_mem=Tableview.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('fname')
        email = request.POST.get('lname')
        mem=Tableview.objects.update(name=name, email=email)
    return render(request, 'table.html', {'update_mem':update_mem})



