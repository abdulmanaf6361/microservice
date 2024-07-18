from django.db import models

# TODO: write here your models

class Email(models.Model):
	sender = models.EmailField()
	receiver = models.EmailField()
	subject = models.CharField(max_length=300)
	body = models.TextField()
