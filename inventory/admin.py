# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Item

#Class to make a customization to admin
class ItemAdmin(admin.ModelAdmin):

	#list_display not set, so record is saved as 'item object' by default
	list_display = ['title', 'amount']

#also need to add the customization to the site by including ItemAdmin as a parameter
admin.site.register(Item, ItemAdmin)
