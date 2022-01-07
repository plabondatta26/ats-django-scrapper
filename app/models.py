from django.db import models


# Create your models here.

class LocationModel(models.Model):
    address = models.CharField(max_length=300, help_text='"address":"8236 SW 1st St, Blue Springs, MO 64014"')
    json_file = models.FileField(upload_to='address_json/', blank=True, null=True)

    def __str__(self):
        return self.address

