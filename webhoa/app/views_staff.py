from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

@login_required
def listCategory(request):
	return render(request, 'staff/category/listcate.html')

@login_required
def addCategory(request):
	return render(request, 'staff/category/formcate.html')

@login_required
def listProduct(request):
	return render(request, 'staff/product/listprod.html')

@login_required
def addProduct(request):
	return render(request, 'staff/product/formprod.html')

def signup(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(username=user.username,password=request.POST.get('password1'))
			login(request, user)
			return redirect('staff-home')
	return render(request, 'registration/signup.html', {'form':form})