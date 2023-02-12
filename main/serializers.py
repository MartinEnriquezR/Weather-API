from rest_framework import serializers
from .models import weatherModel
from datetime import timedelta, datetime


class weatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = weatherModel
        fields = (
            'date_time', 
            'temp_out',
            'hi_temp',                
            'low_temp',                  
            'out_hum',                  
            'dew_pt',                    
            'wind_speed',                
            'wind_dir',
            'wind_run',                  
            'hi_speed',                  
            'hi_dir',
            'wind_chill',                
            'heat_index',                
            'thw_index',                 
            'bar',                       
            'rain',                      
            'rain_rate',                 
            'heat_dd',                   
            'cool_dd',                   
            'in_temp',                   
            'in_hum',                    
            'in_dew',                    
            'in_heat',                   
            'in_emc',                    
            'in_air_density',            
            'wind_samp',                 
            'wind_tx',                   
            'iss_recept',                
            'arc_int',
        ) 

"""Serializer to return the data per day"""
class dayDataSerializer(serializers.Serializer):
    
    #parameters day,month and year
    day = serializers.IntegerField()
    month = serializers.IntegerField()
    year = serializers.IntegerField()

    def validate(self,data):
        #make sure that data exists for the given day
        information = weatherModel.objects.filter(
            date_time__day = data['day'],
            date_time__month = data['month'],
            date_time__year = data['year']
        )
        
        if not information:
            raise serializers.ValidationError('No data available for this day')
        
        return data

    def create(self,data):
        #empty list
        json = []
        
        #filter and organize by date
        records = weatherModel.objects.filter(
            date_time__day = data['day'],
            date_time__month = data['month'],
            date_time__year = data['year']
        ).order_by('date_time')

        for record in records:
            # append this dictionary to an empty list
            json.append({
                'date_time':record.date_time, 
                'temp_out':record.temp_out,
                'hi_temp':record.hi_temp,                
                'low_temp':record.low_temp,                  
                'out_hum':record.out_hum,                  
                'dew_pt':record.dew_pt,                    
                'wind_speed':record.wind_speed,                
                'wind_dir':record.wind_dir,
                'wind_run':record.wind_run,                  
                'hi_speed':record.hi_speed,                  
                'hi_dir':record.hi_dir,
                'wind_chill':record.wind_chill,                
                'heat_index':record.heat_index,                
                'thw_index':record.thw_index,                 
                'bar':record.bar,                       
                'rain':record.rain,                      
                'rain_rate':record.rain_rate,                 
                'heat_dd':record.heat_dd,                   
                'cool_dd':record.cool_dd,                   
                'in_temp':record.in_temp,                   
                'in_hum':record.in_hum,                    
                'in_dew':record.in_dew,                    
                'in_heat':record.in_heat,                   
                'in_emc':record.in_emc,                    
                'in_air_density':record.in_air_density,            
                'wind_samp':record.wind_samp,                 
                'wind_tx':record.wind_tx,                   
                'iss_recept':record.iss_recept,                
                'arc_int':record.arc_int,
            })

        return json 

"""Serializer to return data of three days"""
class threeDaysDataSerializer(serializers.Serializer):
    
    #parameters day,month and year
    day = serializers.IntegerField()
    month = serializers.IntegerField()
    year = serializers.IntegerField()

    def validate(self, data):
        
        day = datetime(data['year'],data['month'],data['day'])  #first day
        
        #get the three days
        for i in range(3):
            info = weatherModel.objects.filter(
                date_time__year =day.year,
                date_time__month =day.month,
                date_time__day= day.day
                )
            if not info:
                raise serializers.ValidationError('No data available for this period of time')
            day += timedelta(days=1)

        return data

    def create(self, data):
        json = []   #place to store the data
        day = datetime(data['year'],data['month'],data['day'])  #first day
        #get the data of the three days
        for i in range(3):
            records = weatherModel.objects.filter(
                date_time__year=day.year,
                date_time__month=day.month,
                date_time__day=day.day
            ).order_by('date_time')
            #add the records in the json
            for record in records:
            # append each dictionary to the list
                json.append({
                    'date_time':record.date_time, 
                    'temp_out':record.temp_out,
                    'hi_temp':record.hi_temp,                
                    'low_temp':record.low_temp,                  
                    'out_hum':record.out_hum,                  
                    'dew_pt':record.dew_pt,                    
                    'wind_speed':record.wind_speed,                
                    'wind_dir':record.wind_dir,
                    'wind_run':record.wind_run,                  
                    'hi_speed':record.hi_speed,                  
                    'hi_dir':record.hi_dir,
                    'wind_chill':record.wind_chill,                
                    'heat_index':record.heat_index,                
                    'thw_index':record.thw_index,                 
                    'bar':record.bar,                       
                    'rain':record.rain,                      
                    'rain_rate':record.rain_rate,                 
                    'heat_dd':record.heat_dd,                   
                    'cool_dd':record.cool_dd,                   
                    'in_temp':record.in_temp,                   
                    'in_hum':record.in_hum,                    
                    'in_dew':record.in_dew,                    
                    'in_heat':record.in_heat,                   
                    'in_emc':record.in_emc,                    
                    'in_air_density':record.in_air_density,            
                    'wind_samp':record.wind_samp,                 
                    'wind_tx':record.wind_tx,                   
                    'iss_recept':record.iss_recept,                
                    'arc_int':record.arc_int,
                })
            day += timedelta(days=1)    #increment the day
        return json

"""Serializer to return data per month"""
class monthDataSerializer(serializers.Serializer):
    
    #parameters
    month = serializers.IntegerField()
    year = serializers.IntegerField()

    def validate(self, data):
        #make sure that data exists for the given month
        first_day = weatherModel.objects.filter(
            date_time__month = data['month'],
            date_time__year = data['year']
        )
        if not first_day:
            raise serializers.ValidationError('No data available for this month')
        return data
    
    def create(self,data):
        json = []

        #get the data of the month
        records = weatherModel.objects.filter(
            date_time__month = data['month'],
            date_time__year = data['year']
        ).order_by('date_time')

        for record in records:
            # append each dictionary to the list
            json.append({
                'date_time':record.date_time, 
                'temp_out':record.temp_out,
                'hi_temp':record.hi_temp,                
                'low_temp':record.low_temp,                  
                'out_hum':record.out_hum,                  
                'dew_pt':record.dew_pt,                    
                'wind_speed':record.wind_speed,                
                'wind_dir':record.wind_dir,
                'wind_run':record.wind_run,                  
                'hi_speed':record.hi_speed,                  
                'hi_dir':record.hi_dir,
                'wind_chill':record.wind_chill,                
                'heat_index':record.heat_index,                
                'thw_index':record.thw_index,                 
                'bar':record.bar,                       
                'rain':record.rain,                      
                'rain_rate':record.rain_rate,                 
                'heat_dd':record.heat_dd,                   
                'cool_dd':record.cool_dd,                   
                'in_temp':record.in_temp,                   
                'in_hum':record.in_hum,                    
                'in_dew':record.in_dew,                    
                'in_heat':record.in_heat,                   
                'in_emc':record.in_emc,                    
                'in_air_density':record.in_air_density,            
                'wind_samp':record.wind_samp,                 
                'wind_tx':record.wind_tx,                   
                'iss_recept':record.iss_recept,                
                'arc_int':record.arc_int,
            })

        return json

"""Serializer to post data"""
class postSerializer(serializers.Serializer):

    #validate every field in the data
    date_time = serializers.DateTimeField()         
    temp_out  = serializers.FloatField(allow_null=True) 
    hi_temp = serializers.FloatField(allow_null=True)                   
    low_temp = serializers.FloatField(allow_null=True)                      
    out_hum  = serializers.IntegerField(allow_null=True)                    
    dew_pt = serializers.FloatField(allow_null=True)                        
    wind_speed = serializers.FloatField(allow_null=True)                    
    wind_dir = serializers.CharField(allow_blank=True)          
    wind_run = serializers.FloatField(allow_null=True)                      
    hi_speed = serializers.FloatField(allow_null=True)                      
    hi_dir = serializers.CharField(allow_blank=True)            
    wind_chill = serializers.FloatField(allow_null=True)                    
    heat_index = serializers.FloatField(allow_null=True)                    
    thw_index = serializers.FloatField(allow_null=True)                     
    bar = serializers.FloatField(allow_null=True)                           
    rain = serializers.FloatField(allow_null=True)                          
    rain_rate = serializers.FloatField(allow_null=True)                     
    heat_dd = serializers.FloatField(allow_null=True)                       
    cool_dd = serializers.FloatField(allow_null=True)                       
    in_temp = serializers.FloatField(allow_null=True)                       
    in_hum = serializers.IntegerField(allow_null=True)                      
    in_dew = serializers.FloatField(allow_null=True)                        
    in_heat = serializers.FloatField(allow_null=True)                       
    in_emc = serializers.FloatField(allow_null=True)                       
    in_air_density = serializers.FloatField(allow_null=True)                
    wind_samp = serializers.IntegerField(allow_null=True)                   
    wind_tx = serializers.IntegerField(allow_null=True)                     
    iss_recept = serializers.FloatField(allow_null=True)                    
    arc_int = serializers.IntegerField(allow_null=True) 

    def validate(self, data):
        #make sure that the data does not already exist
        record = weatherModel.objects.filter(
            date_time__year = data['date_time'].year,
            date_time__month = data['date_time'].month,
            date_time__day = data['date_time'].day,
            date_time__hour = data['date_time'].hour,
            date_time__minute = data['date_time'].minute,
            date_time__second = data['date_time'].second
        )
        if record:
            raise serializers.ValidationError('Data for this date and time already exists')

        return data
    
    def create(self, data):
        #create the record
        record = weatherModel.objects.create(
            date_time = data['date_time'],
            temp_out = data['temp_out'],
            hi_temp = data['hi_temp'],
            low_temp = data['low_temp'],
            out_hum = data['out_hum'],
            dew_pt = data['dew_pt'],
            wind_speed = data['wind_speed'],
            wind_dir = data['wind_dir'],
            wind_run = data['wind_run'],
            hi_speed = data['hi_speed'],
            hi_dir = data['hi_dir'],
            wind_chill = data['wind_chill'],
            heat_index = data['heat_index'],
            thw_index = data['thw_index'],
            bar = data['bar'],
            rain = data['rain'],
            rain_rate = data['rain_rate'],
            heat_dd = data['heat_dd'],
            cool_dd = data['cool_dd'],
            in_temp = data['in_temp'],
            in_hum = data['in_hum'],
            in_dew = data['in_dew'],
            in_heat = data['in_heat'],
            in_emc = data['in_emc'],
            in_air_density = data['in_air_density'],
            wind_samp = data['wind_samp'],
            wind_tx = data['wind_tx'],
            iss_recept = data['iss_recept'],
            arc_int = data['arc_int']
        )
        #return the created data
        response = [{
            'date_time':record.date_time,
            'temp_out':record.temp_out,
            'hi_temp':record.hi_temp,
            'low_temp':record.low_temp,
            'out_hum':record.out_hum,
            'dew_pt':record.dew_pt,
            'wind_speed':record.wind_speed,
            'wind_dir':record.wind_dir,
            'wind_run':record.wind_run,
            'hi_speed':record.hi_speed,
            'hi_dir':record.hi_dir,
            'wind_chill':record.wind_chill,
            'heat_index':record.heat_index,
            'thw_index':record.thw_index,
            'bar':record.bar,
            'rain':record.rain,
            'rain_rate':record.rain_rate,
            'heat_dd':record.heat_dd,
            'cool_dd':record.cool_dd,
            'in_temp':record.in_temp,
            'in_hum':record.in_hum,
            'in_dew':record.in_dew,
            'in_heat':record.in_heat,
            'in_emc':record.in_emc,
            'in_air_density':record.in_air_density,
            'wind_samp':record.wind_samp,
            'wind_tx':record.wind_tx,
            'iss_recept':record.iss_recept,
            'arc_int':record.arc_int,
        }]
        return response
