# Generated by Django 2.2.4 on 2019-08-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoption',
            name='pet_age',
            field=models.IntegerField(max_length=3),
        ),
    ]
