#drf
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
#serializers
from .serializers import *
#models
from .models import *

class allDataWeatherViewSet(viewsets.ReadOnlyModelViewSet):
    """View to get all the weather data"""
    permission_classes = [AllowAny]
    queryset = weatherModel.objects.all()
    serializer_class = weatherSerializer

class dataWeatherViewSet(viewsets.GenericViewSet):
    
    permission_classes = [AllowAny]

    """view to get the data of a given date and time"""
    @action(detail=False, methods=['post'], url_path='data-per-hour')
    def givenHour(self,request):
        #parameters of the function: day, month, year, hour, minute and second
        serializer = hourDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data,status=status.HTTP_200_OK)

    """View to get the data of a given day"""
    @action(detail=False, methods=['post'], url_path='data-per-day')
    def givenDay(self,request,*args,**kwargs):
        #parameters of the function: day, month and year
        serializer = dayDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data,status=status.HTTP_200_OK)

    """view to get the data of three days"""
    @action(detail=False, methods=['post'], url_path='data-of-three-days')
    def nextThreeDays(self,request,*args,**kwargs):
        #parameters of the function: day, month and year
        serializer = threeDaysDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data,status=status.HTTP_200_OK)

    """view to get data of a given month"""
    @action(detail=False, methods=['post'], url_path='data-per-month')
    def dataMonth(self,request,*args,**kwargs):
        #parameters of the function: month, year
        serializer = monthDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data,status=status.HTTP_200_OK)
        
    """view to post data in the system"""
    @action(detail=False, methods=['post'], url_path='post-data')
    def postData(self,request):
        serializer = postSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data,status=status.HTTP_201_CREATED)