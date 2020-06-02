from django.contrib import admin

from .models import Route


class RouteAdmin(admin.ModelAdmin):
    """ Displaying data in the admin page """

    list_display = ('id', 'route_from', 'route_to', 'sacco_name',
                    'morning_fare', 'daytime_fare', 'evening_fare')
    list_display_links = ('id', 'route_from',)
    list_filter = ('sacco_name',)
    search_fields = ('route_from', 'route_to', 'sacco_name')
    list_per_page = 30


admin.site.register(Route, RouteAdmin)
