from django.urls import path
from . import views
from .views import ProductsList

urlpatterns =[
    path('',ProductsList.as_view(),name='home')
]
