from django.db import models
from core.models import Conference

class Speaker(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    profile = models.TextField(max_length=400)
    # pic_url =
    conference = models.ForeignKey(Conference)

    class Meta:
        ordering = ['last_name','first_name']

    def __str__(self):
        return self.full_name

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
