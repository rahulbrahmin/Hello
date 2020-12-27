from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Riddhi Tractors & Equipments"
admin.site.site_title = "Riddhi Tractors Admin Portal"
admin.site.index_title = "Welcome to Riddhi Tractors & Equipments"


urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
]
