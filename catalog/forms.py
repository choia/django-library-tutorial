from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import date, timedelta
from django import forms


class RenewBookForm(forms.Form):
	renewal_date = forms.DateField(help_text="Enter a date between today and 4 weeks (default 3).")

	def clean_renewal_date(self):
		data = self.cleaned_data['renewal_date']

		if data < date.today():
			raise ValidationError(_('Invalidate date - renewal in past'))

		if data > date.today() + timedelta(weeks=4):
			raise ValidationError(_('Invalidate date - renewal more than 4 weeks ahead'))
			
		return data