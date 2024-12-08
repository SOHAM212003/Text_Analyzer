
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def analyze(request):
    #get text
    djtext = request.POST.get('text', 'default')

    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    #check which checkbox is on
    if (removepunc == 'on'):
        punctuations = '''!()-[]{};:'",/.<>\?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuation', 'analyze_text': analyzed}
        djtext = analyzed

    if (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Changed to UpperCase', 'analyze_text': analyzed}
        djtext = analyzed

    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'Removed New Lines', 'analyze_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose': 'Removed Extra Space', 'analyze_text': analyzed}
        djtext = analyzed

    if (charcounter == 'on'):
        count = 0
        for char in djtext:
            if char != ' ':
                count += 1
            analyzed = "Number of Characters are = ", count
        params = {'purpose': 'Characters Counted', 'analyze_text': analyzed}

    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcounter != 'on'):
        return HttpResponse("Error")

    return render(request, 'analyse.html', params)

def about_us(requests):
    return render(requests, 'about_us.html')

def contact_us(requests):
    return render(requests, 'contact_us.html')