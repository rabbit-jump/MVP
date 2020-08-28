"""定义maps_vis的URL模式"""
from django.conf.urls import url
from . import views
#from django.urls import path,re_path

urlpatterns = [
	#主页
	url(r'^$',views.index,name='index'),
	#城市中心
	url(r'^showcity/$',views.showcity,name='showcity'),
	#编辑范围，显示poi集
	url(r'^rangepoi/$',views.rangepoi,name='rangepoi'),
	#re_path('^$',views.index)
	#显示poi
	url(r'^showpoi/$',views.showpoi,name='showpoi'),
	#添加poi
	url(r'^addpoi/$',views.addpoi,name='addpoi'),
]