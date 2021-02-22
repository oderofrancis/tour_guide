from __future__ import unicode_literals
from django.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from twilio.rest import Client

# Create your models here.

# county

class County(models.Model):
    county_nam = models.CharField(max_length=50)
    code = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def _unicode_(self):
    	return self.county_nam

    class Meta:
    	verbose_name_plural="County"


# lodges

class Lodge(models.Model):
    name = models.CharField(max_length=25)
    types = models.CharField(max_length=16)
    geom = models.MultiPointField(srid=4326)


    def _unicode_(self):
    	return self.name


# parks


class Park(models.Model):
    areaname = models.CharField(max_length=120)
    iso3 = models.CharField(max_length=3)
    gisname = models.CharField(max_length=80)
    site_code = models.IntegerField()
    area_sqkm_field = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)


    def _unicode_(self):
    	return self.areaname

# airport

class Airstrip(models.Model):
	fid=models.PositiveIntegerField()
	name=models.CharField(max_length=120)
	geom = models.MultiPointField(srid=4326)

	def _unicode_(self):
		return self.name


# booking

class Booking(models.Model):
	name = models.CharField(max_length=150)
	phone_number = PhoneNumberField(help_text='Contact phone number')
	number_of_slots  = models.PositiveIntegerField()
	where_to_book = models.PointField(srid=4326)
	from_date = models.DateField(default=timezone.now)
	to_date = models.DateField()
	
	
# sending sms
	def save(self,*args,**kwargs): 
		account_sid='AC0533feb40b29ee2c27d2c92c17a18f70'
		auth_token='11af7c11dee00a9343cbccad679846ac'
		client=Client(account_sid,auth_token)

		message= client.messages.create(
	                        body=f'Booking of hotel has been done by {self.name}, at {self.where_to_book}, with {self.number_of_slots} slots to occupy From {self.from_date} to {self.to_date}',
	                        from_='+12057511288',
	                        to='+254791061506'
	                )

		print(message.sid)
		return super().save(*args,**kwargs)

		def _unicode_(self):
			return self.name