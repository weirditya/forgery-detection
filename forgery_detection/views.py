from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *

from forgery_detection.examples.copy_move_detection import detect
from . models import *
#from forgery_detection.examples.example_01 import main
import os
from django.http import JsonResponse

# Create your views here. 
def index(request): 
  
    if request.method == 'POST': 
        form = databaseForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save()
            image_name = database.objects.last()
            print(image_name)
            image_loc = 'media/'+str(image_name)
            print('QQQQQQQQQQQQ$$$$$$$$$$$$$$$$$$$$$$$$$$$QQQQQQQQQQQQQ',image_loc)
            detect.detect(image_loc, 'media/output/', block_size=16)
        


            #SUCCESS
        return redirect('success') 
    else: 
        form = databaseForm() 
    return render(request, 'index.html', {'form' : form}) 
  
  
def success(request): 
    image_name = str(database.objects.last())
    image_name = image_name.split('/')[1]
    #print(image_name)
    f = open('media/result.txt', 'r')
    output = f.readline()
    f.close()
    if output == 'Found pair(s) of Possible Fraud Attack':
        colour = 'red'
    else:
        colour = 'green'
        
    return render(request, 'show_images.html', {'img':image_name, 'output': output, 'colour':colour})






