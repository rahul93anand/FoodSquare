from django.shortcuts import render, HttpResponse,redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


def login_register_page(request):
    return render(request,"login_page.html")


def register_page(request):
    return render(request,"register_page.html")

@api_view(['GET','POST'])
def register(request):
    if request.method == "POST":
        print(request.POST)
        return Response("teri ma ki chut")
    else:
        return redirect("/register_page")


def welcome(request):
    return render(request,'index.html')



def Contact_Me_Form(request):
    incoming_dict=request.POST
    subject_owner="Hey a new message from " + incoming_dict.get("name")
    message_body_owner=incoming_dict.get("message")
    from_owner="foodsquare10@gmail.com"
    to_owner=['rahul93anand@gmail.com']
    send_mail(subject_owner,message_body_owner,from_owner,to_owner)
    return HttpResponse("Heeloo world")

def Registration(request):
    if request.method == "POST":
        print("Hello dude")
    else:
        print("bye dude")

    return HttpResponse("Helloooooo")


