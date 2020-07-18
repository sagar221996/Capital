from django.shortcuts import render

# Create your views here.

def designs(req):
    return render(req,'designs.html')