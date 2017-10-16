from __future__ import unicode_literals
from django.db import models



# Create your models here.

#新增元组用于设置消息类型枚举项

KIND_CHOICE = (
    ('python技术','python技术'),
    ('数据库技术','数据库技术'),
    ('经济学','经济学'),
    ('其他','其他'),
)

class Moment(models.Model):

    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length=20,default='匿名')
    kind = models.CharField(max_length=20,choices=KIND_CHOICE,default=KIND_CHOICE[0])

