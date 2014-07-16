from django.http import HttpResponse
from videos.models import UserDetails
from django import template
from django.template.loader import get_template
from django.template import Context
from function import getHomePageValues
from forms import RegistrationForm


def homepage(request):
		
	loadingTemplate = get_template('homepage.html')
	values = getHomePageValues()
	html = loadingTemplate.render(Context({'video':values}))
	return HttpResponse(html)


def registrationForm(request):
		
	loadingTemplate = get_template('registrationForm.html')
	insertTemplate = RegistrationForm()
	#insertTemplate = "bharath"
	print insertTemplate
	html = loadingTemplate.render(Context({'values':insertTemplate}))
	print html
	return HttpResponse(html)

def submit(request):
	
	print request.GET['firstname']
	print request.GET['lastname']
	print request.GET['city']
	print request.GET['country']
	print request.GET['website']
	print request.GET['email']
	print request.GET['phonenumber']
	print request.GET['userID']
	print request.GET['password']

	
	firstName = request.GET['firstname']
	usercity =  request.GET['city']
	userCountry =  request.GET['country']
	userwebsite =  request.GET['website']
	useremail =  request.GET['email']
	phoneNumber =  request.GET['phonenumber']
	ID =  request.GET['userID']
	userpassword = request.GET['password']
	lastName = request.GET['lastname']

	print "taken all values"
	p1 = UserDetails(firstname = firstName, lastname = lastName,city = usercity,country = userCountry,website = userwebsite,email = useremail,phonenumber = phoneNumber,userID = ID,password = userpassword)
	p1.save()
	print "data saved"
	return HttpResponse("Got ur information. THank you!!")

