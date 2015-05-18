from django.db import models

class Speaker(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    profile = models.TextField()
    # pic_url =

    class Meta:
        ordering = ['last_name','first_name']

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
