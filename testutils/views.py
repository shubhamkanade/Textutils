from django.http import HttpResponse
from django.shortcuts import render

import os

def index(request):
    params = {'name': 'shubham', 'place': 'pune'}
    return render(request, 'index.html', params)

def display(request):
    return render(request, 'show.html')

def contact(request):
    return render(request, 'contact.html')

def analyze(request):

    dtext1 = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount= request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctu = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed = ""
        for ch in dtext1:
            if ch not in punctu:
                analyzed = analyzed + ch


        params = {'purpose': 'remove punctuation', 'analyzed_text': analyzed}
        dtext1 = analyzed

    if capitalize == "on":
        analyzed = ""
        for ch in dtext1:
            analyzed += ch.upper()

        params = {'purpose': 'capitalize', 'analyzed_text': analyzed}
        dtext1 = analyzed

    if newlineremover == "on":
        analyzed = ""
        for ch in dtext1:
            if ch != '\n' and ch!='\r':
                analyzed += ch


        params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
        dtext1 = analyzed

    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(dtext1):
            if not(dtext1[index] == ' ' and dtext1[index + 1] == ' '):
                analyzed += char

        params = {'purpose': 'space remover', 'analyzed_text': dtext1}
        dtext1 = analyzed

    if charcount == "on":
        analyzed = ""
        for ch in dtext1:
            analyzed += 1
        params = {'purpose': 'space remover', 'analyzed_text': analyzed}

    if(removepunc!="on" and newlineremover!="on" and capitalize!="on" and spaceremover!="on"):
        return HttpResponse("error")

    return render(request, 'analyze.html', params)





