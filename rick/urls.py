from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details_chapter/<int:id_capitulo>/', views.details_chapter, name='details_chapter'),
    path('details_character/<int:id_character>/', views.details_character, name='details_character'),
    path('details_location/<int:id_location>/', views.details_location, name='details_location'),
    path('search/', views.search, name='search'),

]