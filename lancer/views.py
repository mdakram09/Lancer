from django.http import HttpResponse
from django.shortcuts import render
from userform.models import Userform


def index(request):
    if request.method=="POST":
        print("We are using post method")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        state =request.POST['state']
        city =request.POST['city']
        road =request.POST['road']
        building =request.POST['building']
        pin =request.POST['pin']
        content =request.POST['content']
        userform=Userform(name=name, email=email, phone=phone, state=state, city=city, road=road, building=building, pin=pin, content=content)
        userform.save()
    return render(request, 'index.html')


