#django library
from django.urls import path,include
# drf library
from rest_framework.routers import DefaultRouter
#import all the views
from .views import *


router = DefaultRouter()
router.register(r'all-weather-data',allDataWeatherViewSet,basename='all-weather-data')
router.register(r'data',dataWeatherViewSet,basename='data')


urlpatterns = [
    path('',include(router.urls))
]

