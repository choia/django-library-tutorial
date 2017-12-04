from django.core.exceptions import ValidateError
from django.utils.translation import ugettext_lazy as _
from datetime import date, timedelta
from django import forms


class RenewBookForm(forms.Form):
	renewal_date = forms.DateField(help_test="Enter a date between today and 4 weeks (default 3).")

	def clean_renewal_date(self):
		data = self.cleaned_date['renewal_date']

		if data < date.today():
			raise ValidateError(_('Invalidate date - renewal in past'))

		if date > date.today() + timedelta(week=4):
			raise ValidateError(_('Invalidate date - renewal more than 4 weeks ahead'))
			
		return data