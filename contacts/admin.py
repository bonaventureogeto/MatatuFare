from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_date', 'message')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_per_page = 30


admin.site.register(Contact, ContactAdmin)
