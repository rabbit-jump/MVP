from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
from .forms import MapcenterForm
from .models import Topic,Entry#首先导入与所需数据相关联的模型
import json

# Create your views here.
def index(request):
	"""地图可视化的主页"""
	return render(request,'maps_vis/index.html')

def showcity(request):
	"""显示指定城市的地图"""
	if request.method !='POST':
		form = MapcenterForm()
	else:
		form = MapcenterForm(request.POST)
		#print(request.POST.get("cityname"))
		cityname=[request.POST.get("cityname")]
		
		print(cityname)
		print("jjajjajajja")
		if form.is_valid():
			# return HttpResponseRedirect(reverse('maps_vis:showcity',{'cityname':json.dumps(cityname),}))
			return render(request,'maps_vis/showcity.html',{'Cityname':json.dumps(cityname),})
	print("return后的信息")
	context = {'form':form}
	return render(request,'maps_vis/showcity.html',context)

def rangepoi(request):
	return render(request,'maps_vis/rangepoi.html')
"""L"""
def showpoi(request):
    alls = Topic.objects.all()
    for all in alls:
        ids = all.id
    t = Topic.objects.get(id=ids)
    print(t)
    entries = t.entry_set.order_by('date_added')
    #context = {'topic': l, 'entries': entries}
    context = {'entries': entries}
    #return render(request, 'maps_vis/all.html', context)
    return render(request, 'maps_vis/showpoi.html', context)

"""X"""
def addpoi(request):
	return render(request, 'maps_vis/addpoi.html')