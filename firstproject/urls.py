from django.conf.urls import url
from django.contrib import admin

# 1) custom
from inventory import views

urlpatterns = [

	# 2) Home page
	url(r'^$', views.index, name='index'),

	# 3) Item page
	url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),

	# 4) admin page
    url(r'^admin/', admin.site.urls),
]
