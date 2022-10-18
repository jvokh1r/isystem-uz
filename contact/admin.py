from django.contrib import admin
from .models import Contact, Apply


class AdminContact(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_solved')


class AdminApply(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Contact, AdminContact)
admin.site.register(Apply, AdminApply)