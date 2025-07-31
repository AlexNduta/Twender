from django.contrib import admin
from .models import Route, Stop

# This allows you to edit stops directly from the routes page

class StopInline(admin.TabularInline):
    model = Stop
    extra = 1 # number of empty stop forms to display

class RouteAdmin(admin.ModelAdmin):
    inlines = [StopInline]


admin.site.register(Route, RouteAdmin)
admin.site.register(Stop) # register stops seperately too
