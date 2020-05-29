from django.shortcuts import get_object_or_404, render
from .models import Route


def route(request, route_id):
    route = get_object_or_404(Route, pk=route_id)

    context = {
        'route': route
    }

    return render(request, 'routes/route.html', context)


def search(request):
    queryset_list = Route.objects.all()

    # route_from
    if 'route_from' in request.GET:
        route_from = request.GET['route_from']
        if route_from:
            queryset_list = queryset_list.filter(
                description__icontains=route_from)

        # route_to
    if 'route_to' in request.GET:
        route_to = request.GET['route_to']
        if route_to:
            queryset_list = queryset_list.filter(route_to__iexact=route_to)

    # Price
    if 'morning_fare' in request.GET:
        morning_fare = request.GET['morning_fare']
        if morning_fare:
            queryset_list = queryset_list.filter(
                morning_fare__lte=morning_fare)

    if 'daytime_fare' in request.GET:
        daytime_fare = request.GET['daytime_fare']
        if daytime_fare:
            queryset_list = queryset_list.filter(
                daytime_fare__lte=daytime_fare)

    if 'evening_fare' in request.GET:
        evening_fare = request.GET['evening_fare']
        if evening_fare:
            queryset_list = queryset_list.filter(
                evening_fare__lte=evening_fare)

    context = {
        'routes': queryset_list,
        'values': request.GET
    }

    return render(request, 'routes/search.html', context)
