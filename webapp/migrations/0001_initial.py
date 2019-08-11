# Generated by Django 2.2.4 on 2019-08-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adoption',
            fields=[
                ('pet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pet_name', models.CharField(max_length=30, null=True)),
                ('pet_breed', models.CharField(max_length=30)),
                ('pet_type', models.CharField(max_length=30)),
                ('pet_gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Dont wish to disclose')])),
                ('pet_age', models.IntegerField()),
                ('pet_email_id', models.CharField(max_length=30)),
                ('pet_bio', models.CharField(max_length=500)),
                ('pet_contact', models.CharField(max_length=500)),
                ('pet_location_address', models.CharField(max_length=500)),
                ('pet_location_longitude', models.CharField(max_length=500)),
                ('pet_location_latitude', models.CharField(max_length=500)),
            ],
        ),
    ]