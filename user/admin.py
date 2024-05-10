from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Course)
admin.site.register(Lession)
admin.site.register(UserCourseLink)
admin.site.register(QuizQuestion)
admin.site.register(QuizResult)

class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('date_joined',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
