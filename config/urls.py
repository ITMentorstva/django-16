
from django.contrib import admin
from django.urls import path
from api.views import api_item
from api.views import api_item_single

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/item', api_item, name='api_item'),
    path('api/item/<int:pk>', api_item_single, name='api_item_single')
]

# GET => api/item/<ID> -> api/item/5

# /api/item -> GET, POST

# REST

# Obican api: /getUsers
# REST mi smo fokusirani na RESURS: /users, a obzirom da pozivamo sa GET metodom nas
# kod zna da je u pitanju uzimanje svih korisnika

# HTTP metode koje koristi REST API
# GET -> Da uzme listu resursa
# POST -> kreiranje novog resursa
# PUT -> Kompletan update ili replace trenutnog/postojeceg resursa
# PATCH -> Odredjeni update, zelim da promenim samo email
# DELETE -> brisanje resursa

# Odgovor / Response
# JSON

# Stateless
# users -> vrati sve korisnike












