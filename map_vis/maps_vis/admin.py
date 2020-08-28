from django.contrib import admin

# Register your models here.
from maps_vis.models import Mapcenter,Userpoi
from maps_vis.models import Topic,Entry#导入要注册的模型map_center

admin.site.register(Topic)#让Django通过管理网站管理我们的模型
admin.site.register(Entry)
admin.site.register(Mapcenter)
admin.site.register(Userpoi)