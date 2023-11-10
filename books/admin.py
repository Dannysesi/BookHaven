from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "genre":
            kwargs["queryset"] = Genre.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class BookHavenAdminSite(AdminSite):
    title_header = 'BookHaven Admin'
    site_header = 'BookHaven Administration'
    index_title = 'BookHaven Site Admin'

admin_site = BookHavenAdminSite(name='BookHaven')

admin_site.register(Book, BookAdmin)
admin_site.register(Genre)
admin_site.register(Review)