from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), #Asosoiy sahifa
    path('contact/', views.contact, name='contact'), #Xabar qoldirish sahifa
    path('about/', views.about, name='about'), #Blog sahifa
    path('services/', views.services, name='services') #Xizmatlar sahifas
]