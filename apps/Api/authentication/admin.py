from django.contrib import admin

from apps.Api.authentication.models import CustomUser

# Register your models here.


admin.site.register(CustomUser)