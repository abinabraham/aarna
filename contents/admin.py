# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Slider, Category, Products

admin.site.register(Slider)
admin.site.register(Category)
admin.site.register(Products)


