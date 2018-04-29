from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from .models import Order

class OrderCreateForm(forms.ModelForm):

	class Meta:
		model = Order
		fields = ('card_number', 'cardholder_name','CVV_code','expiry_date' )

	def clean_card_number(self):
		card_number = self.cleaned_data['card_number']

		if not card_number.isdigit():
			raise forms.ValidationError("Card number can only contain numbers")
		elif len(card_number) != 16:
			raise ValidationError('Card must contain 16 digits')
		return card_number

	def clean_CVV_code(self):
		CVV_code = self.cleaned_data['CVV_code']
		
		if not CVV_code.isdigit():
			raise forms.ValidationError("CVV code can only contain numbers")
		elif len(CVV_code) != 3:
			raise ValidationError('CVV code must contain 3 digits')
		return CVV_code