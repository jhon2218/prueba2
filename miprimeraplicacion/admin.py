from django.contrib import admin
from.models import Tejidomama
# Register your models here.

class TejidomamaAdmin(admin.ModelAdmin):
      list_display = ('partP','temperatura','color','inflamacion')
      
admin.site.register(Tejidomama,TejidomamaAdmin)
