from django.contrib import admin
from .models import Posts, Subjects, User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'password')

admin.site.register(Posts)
admin.site.register(Subjects)
admin.site.register(User)