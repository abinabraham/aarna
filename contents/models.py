# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Slider(models.Model):
    heading = models.CharField("Main Heading", max_length=200)
    subheading = models.CharField("Heading 2", max_length=250,  blank=True)
    details = models.TextField("Description",max_length=500, blank=True)
    url = models.CharField(max_length=500,  blank=True)
    slider1 = models.ImageField("SLider Image", upload_to='static/sliders/', null=True, blank=True)
    price = models.ImageField("Price Image", upload_to='static/sliders/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['updated_at']
    def __str__(self):
        return self.heading          


class Category(models.Model):
    title = models.CharField("Main Heading", max_length=200)
    details = models.TextField("Description",max_length=500, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        ordering = ['updated_at']

    def __str__(self):
        return self.title            


class Products(models.Model):
    category = models.ForeignKey(Category, max_length=500, blank=True, null=True)
    details = models.TextField("Details", max_length=500, blank=True)
    name = models.CharField("Title", max_length=200)
    image = models.ImageField("Image",upload_to='static/avatars/', null=True, blank=True)
    price_original = models.CharField("Original Price", max_length=150, blank=True)
    price_offer = models.CharField("Offer Price", max_length=150, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):              # __unicode__ on Python 2
        return self.name