from django.db import models
from django.utils import timezone
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

class Guest(models.Model):
    first_name = models.TextField(max_length=15, default="")
    last_name = models.TextField(max_length=15, default="")
    message = models.TextField(null=True)
    email = models.EmailField(max_length=70, unique=True)
    attending_wedding = models.BooleanField(default=True)
    attending_reception = models.BooleanField(default=True)
    additional_guests = models.IntegerField(blank=True, null=True, default=1)
    ip_address = models.GenericIPAddressField(default="")
    submission_timestamp = models.DateTimeField(blank=True, null=True)


class IP(models.Model):
	ip_address = models.GenericIPAddressField()
