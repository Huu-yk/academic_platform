from django.db import models

class ConferenceInfo(models.Model):
    name = models.CharField(max_length=100,default='')
    url = models.CharField(max_length=100,default='')
    key_word = models.CharField(max_length=30,default='')
    begin_time = models.DateField(auto_now=False)
    end_time = models.DateField(auto_now=False)
    host_address = models.CharField(max_length=255,default='')
    description = models.TextField()

    class Meta:
        db_table = "ConferenceInfo"