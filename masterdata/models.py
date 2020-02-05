# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SD_creation(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    creation_name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
            return self.name

class MD_creation(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    date_creation = models.CharField(max_length=100,blank=True, null=True)
    def __str__(self):
        return self.name

class Donor(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    amount = models.IntegerField(blank=True,null=True)

class Profile(models.Model):
    profile_name = models.CharField(max_length=100, blank=True, null=True)
    book_id = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)