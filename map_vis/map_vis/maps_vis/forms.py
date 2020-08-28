from django import forms
from .models import Mapcenter

class MapcenterForm(forms.ModelForm):
	class Meta:
		model = Mapcenter
		fields = ['cityname']
		labels ={'cityname':''}