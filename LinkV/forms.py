from django import forms

class RegistrationForm(forms.Form):
	
	firstname = forms.CharField()
	lastname = forms.CharField()
	city = forms.CharField()
	country = forms.CharField()
	website = forms.URLField()
	email = forms.EmailField()
	phonenumber = forms.CharField()
	userID = forms.CharField()
	password = forms.CharField()


