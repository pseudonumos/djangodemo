from django.db import models

# Create your models here.

class Voyage(models.Model):
	departure_hub = models.CharField(max_length=200)
	arrival_hub = models.CharField(max_length=200)
	real_price = models.DecimalField(max_digits=8, decimal_places=2)
	price_tag = models.DecimalField(max_digits=8, decimal_places=2)
	departure_date_time = models.DateTimeField()
	arrival_date_time = models.DateTimeField()
	#departure_time = models.TimeField()
	#arrival_time = models.TimeField()
	#departure_date = models.DateField()
	#arrival_date = models.DateField()
	stops = models.IntegerField()
	transit_time = models.TimeField()
	departure_city = models.CharField(max_length=200)
	arrival_city = models.CharField(max_length=200)
	transportation_type = models.CharField(max_length=200)

        def __unicode__(self):
            return self.departure_city + '->' + self.arrival_city

class Result(models.Model):
	departure_hub = models.CharField(max_length=200)
	arrival_hub = models.CharField(max_length=200)
	real_price = models.DecimalField(max_digits=8, decimal_places=2)
	price_tag = models.DecimalField(max_digits=8, decimal_places=2)
	departure_date_time = models.DateTimeField()
	arrival_date_time = models.DateTimeField()
	stops = models.IntegerField()
	transit_time = models.TimeField()
	departure_city = models.CharField(max_length=200)
	arrival_city = models.CharField(max_length=200)
	train_boolean = models.BooleanField()
	plane_boolean = models.BooleanField()
	bus_boolean = models.BooleanField()
	ferry_boolean = models.BooleanField()
	voyages = models.ManyToManyField(Voyage)
	#https://docs.djangoproject.com/en/dev/ref/models/relations/

        def __unicode__(self):
            return self.departure_city + '->' + self.arrival_city
