from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')

class Breed(models.Model):
    SIZE_CHOICE = (
        ('tiny', 'Tiny'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    )
    NUM_CHOICE = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
    name = models.CharField(max_length=1000, blank=False)
    size = models.CharField(max_length=1000, choices=SIZE_CHOICE)
    friendliness = models.IntegerField(choices=NUM_CHOICE)
    trainability = models.IntegerField(choices=NUM_CHOICE)
    sheddingamount = models.IntegerField(choices=NUM_CHOICE)
    exerciseneeds = models.IntegerField(choices=NUM_CHOICE)

class Dog(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    age = models.IntegerField(max_length=1000, blank=False)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1000, blank=False)
    color = models.CharField(max_length=1000, blank=False)
    favoritefood = models.CharField(max_length=1000, blank=False)
    favoritetoy = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.name)
