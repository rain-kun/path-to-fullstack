from django.contrib import admin
# Register your models here.
from .models import User, Email


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'id',)


admin.site.register(User, UserAdmin)


class EmailAdmin(admin.ModelAdmin):
    list_display = ('sender', 'subject', 'timestamp')


admin.site.register(Email, EmailAdmin)
