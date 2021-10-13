from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
	path('', views.index, name='index'),

	path('about/', views.about, name='about'),

	path('menu/', views.menu, name='menu'),
	path('dish/<str:pk>/', views.dish, name='dish'),

	path('gallery/', views.gallery, name='gallery'),
	path('image/<str:pk>/', views.gallery_img, name='image'),

	path('reservation/', views.reservation, name='reservation'),
	path('reservlist/', views.reservList, name='reservlist'),
	path('delete/<str:pk>/', views.reservDel, name='resdel'),

	path('add_food/', views.addFood, name='add'),
	path('del_food/<str:pk>/', views.deleteFood, name='del'),
	path('edit_food/<str:pk>/', views.editFood, name='edit_food'),

	path('add_gall/', views.addGallery, name='add_gal'),
	path('del_gall/<str:pk>/', views.deleteGallery, name='del_gal'),
	path('edit_gall/<str:pk>/', views.editGallery, name='edit_gal'),

	path('login/', CustomLoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]