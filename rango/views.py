from django.shortcuts import render


from django.http import HttpResponse
def index(request):
    html=  "Rango says hey there partner!"+'<a href="/rango/about">About</a>'
    return HttpResponse(html)


def about(request):
  
    return HttpResponse("Rango says here is the about page.")
