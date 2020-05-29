from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == 'POST':
        route_from = request.POST['listing_id']
        route_to = request.POST['listing']
        user_id = request.POST['user_id']

    contact = Contact(route_from=route_from,
                      route_to=route_to, user_id=user_id)

    contact.save()

    return redirect('/routes/')
