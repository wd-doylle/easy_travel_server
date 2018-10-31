# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TravelUser

# Register your models here.
admin.site.register(TravelUser, UserAdmin)