from django.contrib.auth.models import Permission, User
from django.db import models
from django import forms
from django.core.validators import RegexValidator
from django.utils import timezone


class Receiver(models.Model):
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = models.CharField(validators=[phone_regex], max_length=16)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name + ' - ' + self.phone
