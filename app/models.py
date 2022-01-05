from django.db import models


# Create your models here.

class LocationModel(models.Model):
    address = models.CharField(max_length=300)
    json_file = models.FileField(upload_to='address_json/')

    def __str__(self):
        return self.address

