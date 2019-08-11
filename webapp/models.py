from django.db import models

# Create your models here.

class adoption(models.Model):

    pet_id = models.IntegerField(primary_key = True)
    pet_name = models.CharField(max_length = 30, null = True)
    pet_breed = models.CharField(max_length = 30)
    pet_type = models.CharField(max_length = 30)
    pet_gender = models.IntegerField(choices = ((0,'Male'),(1,'Female'),(2,'Dont wish to disclose')))
    pet_age = models.IntegerField()
    pet_email_id = models.CharField(max_length = 30)
    # pet_images = models.ArrayModelField
    pet_bio = models.CharField(max_length = 500)
    pet_contact = models.CharField(max_length = 500)
    pet_location_address = models.CharField(max_length = 500)
    pet_location_longitude = models.CharField(max_length = 500)
    pet_location_latitude = models.CharField(max_length = 500)


    def __str__(self):
        return self.pet_name


