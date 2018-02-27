from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


# 配置要显示的字段
class ServerInfoAdmin(admin.ModelAdmin):
    list_display = ('ip', 'hostname', 'description', 'system_version',)


admin.site.register(ServerInfo, ServerInfoAdmin)
