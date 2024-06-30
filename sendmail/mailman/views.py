from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        send_mail(name, message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
    return render(request,'index.html')