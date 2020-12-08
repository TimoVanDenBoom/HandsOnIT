from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Business(models.Model):
	business_name = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	image = models.ImageField(null=True)
	creation_date = models.DateField(auto_now_add=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

	def __unicode__(self):
		return self.business_name

class Freelancer(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	image = models.ImageField(null=True)
	creation_date = models.DateField(auto_now_add=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

	def __unicode__(self):
		return self.first_name + " " + self.last_name