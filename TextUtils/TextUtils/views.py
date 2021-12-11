# created file by NAUSHAD
import re

from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')
    #return HttpResponse('hello naushad bhai')

def analyze(request):
    print('analyze')
    #get text area
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if len(djtext)==0:
        return render(request, 'error.html')
    #analyze text area
    if removepunc=='on':
        #analyzed=re.sub('[^A-Za-z0-9]*', '', djtext)
        analyzed = re.sub('[^A-Za-z0-9|\s]*', '', djtext)
        params = {'purpose': 'Punchuation Removed', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyzed.html', params)
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params['purpose']=params['purpose']+','+'Change To Uppercase'
        params['analyzed_text']=analyzed
        #params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyzed.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                analyzed = analyzed + " "
        params['purpose'] = params['purpose'] + ',' + 'Removed NewLines'
        params['analyzed_text'] = analyzed
        #params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text

        djtext = analyzed
        # return render(request, 'analyzed.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params['purpose'] = params['purpose'] + ',' + 'Removed NewLines'
        params['analyzed_text'] = analyzed
        #params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyzed.html', params)

    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on') :
        return render(request, 'error.html')
        #return HttpResponse("<h1>Error !! <br/> <a href='/'>back</a> </h1>")

    return render(request, 'analyzed.html', params)
def removepunch(request):
    return HttpResponse('removepunch')