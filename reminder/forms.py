from django import forms
from reminder.models import Receiver
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

class RegisterForm(forms.ModelForm):
	
	class Meta:
		model = Receiver
		fields = ['name','phone']
		labels = {'name': _('Name'),'phone': _('Contact No. (with country code)'),}