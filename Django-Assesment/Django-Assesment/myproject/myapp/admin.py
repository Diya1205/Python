from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Member, Watchman, Notice, Event, Transaction, Visitor

# Register CustomUser with the admin site
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'user_type', 'is_approved', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type', 'is_approved')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Member)
admin.site.register(Watchman)
admin.site.register(Notice)
admin.site.register(Event)
admin.site.register(Transaction)
admin.site.register(Visitor)