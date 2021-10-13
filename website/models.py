from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Food(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	ingridient = models.TextField()
	extra = models.TextField(blank=False)
	image = models.ImageField(upload_to='food')

	def __str__(self):
		return self.name

class Gallery(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='gallery')
	description = models.TextField()

	def __str__(self):
		return self.name
 
class Reservation(models.Model):
	name = models.CharField(max_length=100)
	phone = PhoneNumberField()
	persons = models.CharField(max_length=2)
	date = models.DateField()

	def __str__(self):
		return self.name