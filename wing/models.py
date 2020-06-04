from django.db import models

# Create your models here.
class Item(models.Model):
	itemnum = models.IntegerField();
	sizelist = models.CharField(max_length=100);
	price = models.IntegerField();
	brand = models.CharField(max_length=100);
	img = models.ImageField(upload_to = 'pics');