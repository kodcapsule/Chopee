# from django.shortcuts import render

from django.http import HttpResponse



def homePage(request):    
    html = "<html><body> <h1> Home Page </h1> </body></html>" 
    return HttpResponse(html)
