from django.contrib import admin

from .models import Profile,Location
from localflavor.in_.forms import INZipCodeField
class ProfileAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    zip_code = INZipCodeField(required=True)

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Location,LocationAdmin)