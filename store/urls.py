from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name='about'),
    path('clients/', views.clients, name='clients'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('strength/', views.strength, name='strength'),
    path('products/', views.products, name='products'),
    path('ballbearing/', views.ballbearing, name='ballbearing'),
    path('nut_bolt/', views.nut_bolt, name='nut_bolt'),
    path('hosepipe/', views.hosepipe, name='hosepipe'),
    path('measuringinstruments/', views.measuringinstruments, name='measuringinstruments'),
    path('grindingwheels/', views.grindingwheels, name='grindingwheels'),
    path('circlips/', views.circlips, name='circlips'),
    path('handtools/', views.handtools, name='handtools'),
]
