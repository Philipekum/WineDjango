from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('analyzer/', analyzer, name='analyzer'),
    path('about/', about, name='about'),
]
