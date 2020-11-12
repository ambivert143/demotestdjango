from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product
from django.views.generic import CreateView, UpdateView
# Create your views here.
def indexhome(request):
	productName = request.GET.get('productName', '')
	productList = Product.objects.filter(name__icontains=productName)
	context = {
		'productList':productList,
		'productName':productName,
	}
	return render(request, 'index_home.html', context)

class ProductCreateView(CreateView):
	model = Product
	fields = '__all__'
	template_name = 'product_form.html'
	success_url = '/'

class ProductUpdateView(UpdateView):
	model = Product
	fields = '__all__'
	template_name = 'product_form.html'
	success_url = '/'