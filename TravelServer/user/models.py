# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class TravelUser(AbstractUser):
    email = models.CharField(max_length=40, unique=True)
    username = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]



class Route(models.Model):
    route = models.CharField(max_length=800)
    description = models.CharField(max_length=8000)
    route_id = models.CharField(max_length=100,unique=True)
    user = models.ForeignKey(TravelUser, on_delete=models.CASCADE)
