from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotAllowed,Http404
from django.core.mail import send_mail
from .settings import EMAIL_HOST_USER
from django.views.decorators.csrf import csrf_exempt

def portfolio(request):
    return render(request,'portfolio.html')

def valid_data(name,email,message):
    check = 0
    if len(name)>0 and len(email)>=10 and len(message)>10 and '@' in email and '.' in email and email.find(".")>email.find("@"):
        check = 1
    return check

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        check = valid_data(name,email,message)
        if check!=0:
            full_message = f"Name = {name}\nEmail = {email}\n\n{message}"
            send_mail("Someone wants to contact with you",full_message,EMAIL_HOST_USER,['manindermatharu2001@gmail.com'],fail_silently=False)
            return HttpResponse("Success")
        else:
             return HttpResponse("Something wrong")
    raise Http404