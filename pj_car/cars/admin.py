from django.contrib import admin
from cars.models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    # use fieldsets to group together fields
    fieldsets = [
        ('TIME INFORMATION', {'fields': ['year']}),
        ('NAME', {'fields': ['brand']})
    ]
       
admin.site.register(Car, CarAdmin)
