from django.db import models
from accounts.models import Account

# Create your models here.

class Address(models.Model):
    Full_name = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    zip_code = models.IntegerField(null=True)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.Full_name
    
    # def save(self, *args, **kwargs):
    #     if all([self.city, self.country]) is None:
    #         self.city, self.country = get_address_from_lat_long(self.latitude, self.longitude)
    #     elif all([self.latitude, self.longitude]) is None:
    #         # using the str(self) will return the full address, which google maps has endpoint for
    #         self.latitude, self.longitude = get_lat_long_from_address(str(self))