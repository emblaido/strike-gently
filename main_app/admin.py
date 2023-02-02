from django.contrib import admin
from .models import Journal 
from .models import Therapy
from .models import Member
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Member

admin.site.register(Journal)
admin.site.register(Therapy)
admin.site.register(Member)

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)


class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'member'

class UserAdmin(BaseUserAdmin):
    inlines = (MemberInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
  
