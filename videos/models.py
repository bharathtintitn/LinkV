from django.db import models

class UserDetails(models.Model):
	firstname = models.CharField(max_length = 30)
	lastname = models.CharField(max_length = 30)
	city = models.CharField(max_length = 30)
	country = models.CharField(max_length = 30)
	website = models.URLField()
	email = models.EmailField()
	phonenumber = models.CharField(max_length = 15)
	userID = models.CharField(max_length = 10)
	password = models.CharField(max_length = 10)

	def __unicode__(self):
		return u'%s %s %s ' %(self.firstname,self.lastname,self.email)


class VideoDetails(models.Model):
	title = models.CharField(max_length = 30)
	description = models.CharField(max_length = 100)
	keywords = models.CharField(max_length = 200)
	timestamp = models.DateField()
	userID = models.ForeignKey(UserDetails)
	videoID = models.CharField(max_length = 100)

	def __unicode__(self):
		return u'%s %s %s ',(self.title,self.description,self.timestamp)
	

# Create your models here.
