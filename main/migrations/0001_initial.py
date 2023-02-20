# Generated by Django 4.1.6 on 2023-02-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weatherModel',
            fields=[
                ('date_time', models.DateTimeField(primary_key=True, serialize=False)),
                ('temp_out', models.FloatField(blank=True, null=True)),
                ('hi_temp', models.FloatField(blank=True, null=True)),
                ('low_temp', models.FloatField(blank=True, null=True)),
                ('out_hum', models.FloatField(blank=True, null=True)),
                ('dew_pt', models.FloatField(blank=True, null=True)),
                ('wind_speed', models.FloatField(blank=True, null=True)),
                ('wind_dir', models.CharField(blank=True, max_length=10)),
                ('wind_run', models.FloatField(blank=True, null=True)),
                ('hi_speed', models.FloatField(blank=True, null=True)),
                ('hi_dir', models.CharField(blank=True, max_length=10)),
                ('wind_chill', models.FloatField(blank=True, null=True)),
                ('heat_index', models.FloatField(blank=True, null=True)),
                ('thw_index', models.FloatField(blank=True, null=True)),
                ('bar', models.FloatField(blank=True, null=True)),
                ('rain', models.FloatField(blank=True, null=True)),
                ('rain_rate', models.FloatField(blank=True, null=True)),
                ('heat_dd', models.FloatField(blank=True, null=True)),
                ('cool_dd', models.FloatField(blank=True, null=True)),
                ('in_temp', models.FloatField(blank=True, null=True)),
                ('in_hum', models.FloatField(blank=True, null=True)),
                ('in_dew', models.FloatField(blank=True, null=True)),
                ('in_heat', models.FloatField(blank=True, null=True)),
                ('in_emc', models.FloatField(blank=True, null=True)),
                ('in_air_density', models.FloatField(blank=True, null=True)),
                ('wind_samp', models.FloatField(blank=True, null=True)),
                ('wind_tx', models.FloatField(blank=True, null=True)),
                ('iss_recept', models.FloatField(blank=True, null=True)),
                ('arc_int', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'weather',
            },
        ),
    ]
