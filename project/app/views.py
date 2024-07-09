from django.shortcuts import render
from datetime import datetime
from app.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def MutualFunds(request):
    return render(request,'MutualFunds.html')
def Post(request):
    return render(request,'Post.html')
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        add=request.POST.get('add')
        contact=Contact(name=name,email=email,phone=phone,add=add,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
