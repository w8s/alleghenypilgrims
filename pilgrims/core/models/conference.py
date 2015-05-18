from django.db import models
from localflavor.us.models import USStateField, USZipCodeField
from datetime import datetime

class Conference(models.Model):

    theme = models.CharField(max_length=255, blank=True, null=True)
    date_start = models.DateField()
    date_end = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    is_current = models.BooleanField(default=False)

    location_address_1 = models.CharField(max_length=100,
                                            blank=True,
                                            null=True)
    location_address_2 = models.CharField(max_length=255,
                                            blank=True,
                                            null=True)
    location_city = models.CharField(max_length=25, blank=True, null=True)
    location_state = USStateField(blank=True, null=True)
    location_zip = USZipCodeField(blank=True, null=True)
    location_name = models.TextField(blank=True, null=True)

    map_link = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return "%s - Theme: %s" % (self.date_start.strftime("%Y"), self.theme)


# class Organization(models.Model):

#     name = models.CharField(max_length=150)

#     def __str__(self):
#         return self.name
