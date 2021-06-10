from django.shortcuts import render,redirect

# from django.http import HttpResponse

#Random Generation
import random

def home(request):
    #Rendering HTML template
    return render(request, 'generator/index.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('specialcharacters'):
        characters.extend(list('!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length'))

    password_generated = ''

    for i in range(length):
        password_generated+=random.choice(characters)

    return render(request,'generator/index.html',{'password_generated':password_generated})
