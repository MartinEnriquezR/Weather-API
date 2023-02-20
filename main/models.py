from django.db import models

# Create your models here.
class weatherModel(models.Model):
    date_time = models.DateTimeField(primary_key=True)                  #datetime field
    temp_out  = models.FloatField(blank=True,null=True)                     #float field
    hi_temp = models.FloatField(blank=True,null=True)                       #float field
    low_temp = models.FloatField(blank=True,null=True)                      #float field
    out_hum  = models.FloatField(blank=True,null=True)                      #float field
    dew_pt = models.FloatField(blank=True,null=True)                        #float field
    wind_speed = models.FloatField(blank=True,null=True)                    #float field
    wind_dir = models.CharField(max_length=10,blank=True)               #char field
    wind_run = models.FloatField(blank=True,null=True)                      #float field
    hi_speed = models.FloatField(blank=True,null=True)                      #float field
    hi_dir = models.CharField(max_length=10,blank=True)                 #char field
    wind_chill = models.FloatField(blank=True,null=True)                    #float field
    heat_index = models.FloatField(blank=True,null=True)                    #float field
    thw_index = models.FloatField(blank=True,null=True)                     #float field
    bar = models.FloatField(blank=True,null=True)                           #float field
    rain = models.FloatField(blank=True,null=True)                          #float field
    rain_rate = models.FloatField(blank=True,null=True)                     #float field
    heat_dd = models.FloatField(blank=True,null=True)                       #float field
    cool_dd = models.FloatField(blank=True,null=True)                       #float field
    in_temp = models.FloatField(blank=True,null=True)                       #float field
    in_hum = models.FloatField(blank=True,null=True)                        #float field
    in_dew = models.FloatField(blank=True,null=True)                        #float field
    in_heat = models.FloatField(blank=True,null=True)                       #float field
    in_emc = models.FloatField(blank=True,null=True)                        #float field
    in_air_density = models.FloatField(blank=True,null=True)                #float field
    wind_samp = models.FloatField(blank=True,null=True)                     #float field
    wind_tx = models.FloatField(blank=True,null=True)                       #float field
    iss_recept = models.FloatField(blank=True,null=True)                    #float field
    arc_int = models.FloatField(blank=True,null=True)                       #float field
    
    class Meta:
        db_table = 'weather'
        
#useful commands
# python manage.py makemigrations main
# python manage.py migrate main