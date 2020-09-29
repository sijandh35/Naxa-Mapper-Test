from django.contrib import admin
from user.models import User


class CustomAdmin(admin.ModelAdmin):
    model = User

admin.site.register(User, CustomAdmin)