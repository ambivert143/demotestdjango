from django.urls import path
from .views import *
from django.urls import include
from .views_staff import *

urlpatterns = [
	path('', indexhome, name='home'),
	path('create_product', ProductCreateView.as_view(), name='create-product'),
	path('update_product/<pk>', ProductUpdateView.as_view(), name='update-product'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('list_category', listCategory, name='list-category'),
	path('accounts/signup', signup),
	path('staff/add_category', addCategory),
	path('staff/list_product', listProduct),
	path('staff/add_product', addProduct),
]