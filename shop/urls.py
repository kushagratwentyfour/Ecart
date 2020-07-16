from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='ShopHome'),
    path("about",views.about,name='aboutUs'),
    path("contact/",views.contact,name='contactUs'),
    path("tracker",views.tracker,name='trackingUs'),
    path("search",views.search,name='search'),
    path("products/<int:myid>",views.productView,name='productView'),
    path("checkout",views.checkout,name='checkout'),

]
