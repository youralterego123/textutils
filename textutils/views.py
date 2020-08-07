# I have created this file- deepayan
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def analyze(request):
    
    djtext=request.POST.get('text','please enter a text')
    removepunc=request.POST.get('removepunc','off')
    capitalize=request.POST.get('capitalize','off')
    ExtreSpaceRemover=request.POST.get('Extre Space Remover','off')
    newline=request.POST.get('newline','off')
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed= ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'analyze':'Remove Punctuations', 'analyzetext':analyzed}
        
        djtext=analyzed    
    if capitalize=="on":
        analyzed= ""
        for char in djtext:
            if char in djtext:
                analyzed =analyzed + char.upper()
        params={'analyze':'Capitalize', 'analyzetext':analyzed}
        
        djtext=analyzed
    if ExtreSpaceRemover=="on":
        analyzed= ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
              analyzed = analyzed + char
        params={'analyze':'Extra Sapce Remover', 'analyzetext':analyzed}
        
        djtext=analyzed
    if newline=="on" :
        analyzed= ""
        for char in djtext:
            if char == '.':
                analyzed= analyzed + char
                analyzed= analyzed + '\n'
            else:
                analyzed= analyzed + char    
        params={'analyze':'NewLine', 'analyzetext':analyzed}
        
        djtext=analyzed
        #return render(request, 'analyze.html', params)           
    if(removepunc !="on" and capitalize !="on" and ExtreSpaceRemover !="on" and newline !="on"):
        return render(request, 'error.html')

    return render(request, 'analyze.html', params)
     
          
   

  


    
   