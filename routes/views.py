from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Route


def index(request):
    routes = Route.objects.all()

    context = {
        'routes': routes
    }

    return render(request, 'routes/route.html', context)


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
                route_from__icontains=route_from)

        # route_to
    if 'route_to' in request.GET:
        route_to = request.GET['route_to']
        if route_to:
            queryset_list = queryset_list.filter(route_to__icontains=route_to)

    context = {
        'routes': queryset_list,
        'values': request.GET
    }

    return render(request, 'routes/search.html', context)
