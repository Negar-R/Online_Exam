from django.contrib import admin
from .models import Profile , Question_Profile

# Register your models here.

admin.site.register(Profile)
# admin.site.register(Question_Profile)

@admin.register(Question_Profile)
class Question_ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ("is_correct" ,)