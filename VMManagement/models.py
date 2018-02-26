from django.db import models

# Create your models here.

from django.db import models


# 服务器信息类
class ServerInfo(models.Model):
    ip = models.CharField(max_length=15)  # 服务器IP
    password = models.CharField(max_length=15)  # 服务器root密码
    hostname = models.CharField(max_length=15)  # 服务器主机名
    cpu_thread = models.IntegerField()  # cpu线程数
    description = models.CharField(max_length=15)  # 用途描述
    system_version = models.CharField(max_length=30)  # 系统版本
    disk = models.CharField(max_length=30)  # 磁盘信息
    memory = models.CharField(max_length=30)  # 内存信息
    apps = models.CharField(max_length=30)  # 运行的app
