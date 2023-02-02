from django.contrib import admin
from .models import Journal 
from .models import Therapy
from .models import Member

admin.site.register(Journal)
admin.site.register(Therapy)
admin.site.register(Member)
#admin.site.unregister(Member)

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
