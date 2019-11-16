from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Movie(models.Model):
    m_name = models.CharField(max_length=200,blank=True,null=True)
    d_name = models.CharField(max_length=200,blank=True,null=True)
    actor = models.CharField(max_length=200,blank=True,null=True)
    movie_id = models.IntegerField(blank=True,null=True)
    budget = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.m_name


class Profile(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField( blank=True, null=True)
    phone_num = models.IntegerField( blank=True, null=True)
    
    def __str__(self):
        return self.name


class MovieFeedback(models.Model):
    profile = models.ForeignKey(Profile, blank=True, null=True)
    movie = models.ForeignKey(Movie, blank=True, null=True)
    rating = models.IntegerField()



    def __str__(self):
        return "%s--%s"%(self.profile.name,self.movie.m_name)

class Donor(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    amount = models.IntegerField(null=True)

    def __str__(self):
        return self.name