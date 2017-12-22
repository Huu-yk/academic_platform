from django.db import models

# Create your models here.
class ConferenceInfo(models.Model):
    conference_name = models.CharField(max_length=100,default='')
    key_word = models.CharField(max_length=30,default='')
    begin_time = models.DateField(auto_now=False)
    end_time = models.DateField(auto_now=False)
    host_address = models.CharField(max_length=255,default='')
    description = models.TextField()
