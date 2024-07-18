#from django.db import models #for sql
from django.db import models


# TODO: write here your models
import json

class Order(models.Model):
	total = models.FloatField()
	customer_name = models.CharField(max_length=100)
	customer_email = models.CharField(max_length=100)
	items = models.TextField(default='[]')


	def set_items(self, items):
		self.items = json.dumps(items)

	def get_items(self):
		return json.loads(self.items)
