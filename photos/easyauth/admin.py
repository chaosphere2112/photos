from django.contrib import admin

# Register your models here.
from .models import LoginToken

@admin.register(LoginToken)
class LoginTokenAdmin(admin.ModelAdmin):
	pass
