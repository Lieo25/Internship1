from django.shortcuts import render, redirect
from googletrans import Translator

from .models import Multilangapp

def home(request):
    # Retrieve train details from the database
    trainobj = Multilangapp.objects.all()
    return render(request, 'home.html', {'trainobj': trainobj})
def insert(request):
    if request.method == 'POST':
        # Retrieve train details from the form
        train_No = request.POST.get('train_No')
        train_name = request.POST.get('train_name')
        train_source = request.POST.get('train_source')
        train_destn = request.POST.get('train_destn')
        arrivaldatatime = request.POST.get('arrivaldatatime')
        platformNo = request.POST.get('platformNo')

        # Save train details
        trainobj = Multilangapp(
            train_No=train_No,
            train_name=train_name,
            train_source=train_source,
            train_destn=train_destn,
            arrivaldatatime=arrivaldatatime,
            platformNo=platformNo
        )
        trainobj.save()

        return redirect('/multilangapp/translate/')

    return render(request, 'insert.html')
# views.py



def translate_tamil(request):
    user_language=request.LANGUAGE_CODE
    translator = Translator()
     
    trainobj = Multilangapp.objects.all()
    translated_trainobj = []
    if request.method == 'POST':
        la=request.POST.get('language')
        
    
    for train in trainobj:
        translated_train= {
        'train_No' : train.train_No,
        'train_name' : translator.translate(train.train_name,src='en',dest=la).text,
        'train_source' : translator.translate(train.train_source,src='en',dest=la).text,
        'train_destn' : translator.translate(train.train_destn,src='en',dest=la).text,
        'arrivaldatatime' : train.arrivaldatatime,
        'platformNo' : train.platformNo,
            }

        translated_trainobj.append(translated_train)   
    return render(request, 'home.html', {'trainobj': translated_trainobj})
