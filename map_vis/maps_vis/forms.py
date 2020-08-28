from django import forms
from .models import Mapcenter,Userpoi

class MapcenterForm(forms.ModelForm):
	class Meta:
		model = Mapcenter
		fields = ['cityname']
		labels ={'cityname':''}


class UserpoiForm(forms.ModelForm):
	class Meta:
		model = Userpoi
		fields =['upoiname','upoilog','upoilat']
		labels={'upoiname':'','upoilog':'','upoilat':''}