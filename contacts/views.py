from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        route_from = request.POST['route_from']
        route_to = request.POST['route_to']
        fare = request.POST['fare']
        sacco_name = request.POST['sacco']
        message = request.POST['message']
        user_id = request.POST['user_id']

        contact = Contact(name=name, email=email, phone=phone, route_from=route_from,
                          route_to=route_to, fare=fare, sacco_name=sacco_name, message=message, user_id=user_id)

        contact.save()

        messages.success(
            request, "Your message has been submitted. We'll get back to you soon.")

    return render(request, 'pages/contact.html')
