from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
import datetime
#from django.contrib.admin.widgets import AdminDateWidget

class usernameForm(forms.Form):
	username=forms.CharField(max_length=30)



class DateForm(forms.Form):
	date=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(datetime.date.today().year-1, datetime.date.today().year + 10)))


class UsernameAndDateForm(forms.Form):
	username=forms.CharField(max_length=30)
	date_from=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(datetime.date.today().year-1, datetime.date.today().year + 10)))
	date_to=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(datetime.date.today().year-1, datetime.date.today().year + 10)))


class DateForm_2(forms.Form):
	date_from=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(datetime.date.today().year-1, datetime.date.today().year + 10)))
	date_to=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(datetime.date.today().year-1, datetime.date.today().year + 10)))

       
