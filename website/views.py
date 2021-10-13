from django.shortcuts import render, redirect
from .models import Food, Gallery, Reservation
from .forms import Booking, AddForm, GalleryForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.

def index(request):

	context = {}
	return render(request, 'website/index.html', context)

def about(request):

	context = {}
	return render(request, 'website/about.html', context)

def gallery(request):
	gallerys = Gallery.objects.all()

	context = {'gallerys': gallerys}
	return render(request, 'website/gallery.html', context)

def gallery_img(request, pk):
	gallery = Gallery.objects.get(id=pk)

	context = {'gallery': gallery}
	return render(request, 'website/image.html', context)

def menu(request):
	dishes = Food.objects.all()

	context = {'dishes': dishes}
	return render(request, 'website/menu.html', context)

def dish(request, pk):
	dish = Food.objects.get(id=pk)

	context = {'dish': dish}
	return render(request, 'website/dish.html', context)

def reservation(request):
	form = Booking()

	if request.method == 'POST':
		form = Booking(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

		msg = 'Thank you, your request accepted, we will call you back!'
		messages.success(request, msg)

	context = {'form': form}
	return render(request, 'website/reservation.html', context)

def reservList(request):

	reservs = Reservation.objects.all()

	context = {'reservs': reservs}
	return render(request, 'website/reservlist.html', context)

def reservDel(request, pk):
	reserv = Reservation.objects.get(id=pk)

	if request.method == "POST":
		reserv.delete()
		return redirect('reservlist')

	context = {'reserv': reserv}
	return render(request, 'website/resdel.html', context)

def addFood(request):
	form = AddForm()

	if request.method == 'POST':
		form = AddForm(request.POST, request.FILES)

		# print('form:', form)

		if form.is_valid():
			form.save()
		return redirect('menu')

	context = {'form': form}
	return render(request, 'website/add_food.html', context)

def editFood(request, pk):
	dish = Food.objects.get(id=pk)
	form = AddForm(instance=dish)

	if request.method == 'POST':
		form = AddForm(request.POST, instance=dish)
		if form.is_valid():
			form.save()
			return redirect('dish')

	context = {'dish': dish, 'form': form}
	return render(request, 'website/edit_food.html', context)

def deleteFood(request, pk):
	food = Food.objects.get(id=pk)

	if request.method == 'POST':
		food.delete()
		return redirect('menu')

	context = {"food": food}
	return render(request, 'website/del_food.html', context)

def addGallery(request):
	form = GalleryForm()

	if request.method == 'POST':
		form = GalleryForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('gallery')

	context = {'form': form}
	return render(request, 'website/add_gal.html', context)

def editGallery(request, pk):
	gal = Gallery.objects.get(id=pk)
	form = GalleryForm(instance=gal)

	if request.method == 'POST':
		form = GalleryForm(request.POST, instance=gal)
		if form.is_valid():
			form.save()
			return redirect('gallery')

	context = {'gal': gal, 'form': form}
	return render(request, 'website/edit_gal.html', context)

def deleteGallery(request, pk):
	gal = Gallery.objects.get(id=pk)

	if request.method == 'POST':
		gal.delete()
		return redirect('menu')

	context = {"gal": gal}
	return render(request, 'website/del_gal.html', context)

class CustomLoginView(LoginView):
	template_name = 'website/login.html' 
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('index')
