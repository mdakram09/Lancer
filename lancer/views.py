from django.http import HttpResponse
from django.shortcuts import render
from userform.models import Userform
from django.contrib import messages

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
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Userform(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
        userform=Userform(name=name, email=email, phone=phone, state=state, city=city, road=road, building=building, pin=pin, content=content)
        userform.save()
    return render(request, 'index.html')





from workforusform.models import Workforusform

def workforusform(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        paddress=request.POST['paddress']
        pan=request.POST['pan']
        date=request.POST['date']
        experience =request.POST['experience']
        if len(name)<2 or len(email)<3 or len(phone)<10:
            messages.error(request, "Please fill the form correctly")
        else:
            workforusform=Workforusform(name=name,phone=phone, email=email,paddress=paddress,pan=pan,date=date,  experience=experience)
            workforusform.save()
            messages.success(request, "Your message has been successfully sent")
        workforusform=Workforusform(name=name,phone=phone, email=email,paddress=paddress,pan=pan,date=date,  experience=experience)
        workforusform.save()
    return render(request, "workWithUs.html")

