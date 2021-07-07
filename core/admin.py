from django.contrib import admin

# Register your models here.
from .models import User, Habit, Record

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Habit)
admin.site.register(Record)