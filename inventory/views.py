# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# 1) Http404
from django.http import Http404
from inventory.models import Item 

# 2) Index function for home page
def index(request):

	# return the items if there is stock
	items = Item.objects.exclude(amount=0)

	#return render, creates Http response and wires to Template.
	#the third parameter is a dictionary
	return render(request, 'inventory/index.html', {
			#Keys are what we want displayed
			#Values are the 'items' defined in the view on line 12

				'items': items,
		})

# 3) item_detail function for item page
def item_detail(request, id):
	try:  
		# The id on the right is the one that is passed in as a parameter
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')

	return render(request, 'inventory/item_detail.html', {
			'item': item,
		})