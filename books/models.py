from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher')
    publication_data = models.DateField()
    
    def __unicode__(self): # __str__ on Python3
        return self.title

class Author(models.Model):
    salutation = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __unicode__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()
    
    def __unicode__(self):
        return self.name