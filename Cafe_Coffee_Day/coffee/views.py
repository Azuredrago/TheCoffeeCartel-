from django.shortcuts import render

def index(request):
    return render(request,"index.html")
def signup(request):
    return render(request,"signup.html")
def handlelogin(request):
    return render(request,"handlelogin.html")

# Create your views here.
