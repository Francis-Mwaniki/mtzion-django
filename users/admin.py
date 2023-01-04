from django.contrib import admin
from .models import CustomUser, SubscribedUsers
class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(SubscribedUsers, SubscribedUsersAdmin)
