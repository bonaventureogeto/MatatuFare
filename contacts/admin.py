from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'route_from',
                    'route_to', 'fare', 'sacco_ame')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_per_page = 30


admin.site.register(Contact, ContactAdmin)
