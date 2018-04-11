from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Case(models.Model):
	created_time=models.DateTimeField()
	level=models.CharField(max_length=10)
	description=models.TextField()
	action=models.TextField()
	cost=models.CharField(max_length=100)
	casualties=models.CharField(max_length=100)
	status=models.CharField(max_length=10,blank=True)
	comment=models.CharField(max_length=100,blank=True)
	approved = models.NullBooleanField(null = True)
	def __str__(self):
		return self.level+"|"+str(self.description)

class User(models.Model):
    userName=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
