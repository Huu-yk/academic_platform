from django.db import models

class ConferenceInfo(models.Model):
    Conf_name = models.CharField(max_length=255,default='')
    Crawl_url = models.CharField(max_length=255, default='')
    Conf_ID = models.IntegerField()
    Abbreviation = models.CharField(max_length=30, default='')
    Conf_sponsors = models.CharField(max_length=255,default='')
    Web_site = models.CharField(max_length=255,default='')
    Begin_date = models.DateField(auto_now=False)
    End_date = models.DateField(auto_now=False)
    Location = models.CharField(max_length=255,default='')
    Contact = models.CharField(max_length=255,default='')
    Introduction = models.TextField()
    Attendance = models.IntegerField()
    Detail_paper = models.CharField(max_length=255,default='')
    Important_dates = models.CharField(max_length=255,default='')

    class Meta:
        db_table = "ConferenceInfo"