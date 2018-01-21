from rest_framework import serializers
from .models import ConferenceInfo

class ConferenceSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceInfo
        fields = ('id', 'Conf_name', 'Crawl_url', 'Conf_ID', 'Abbreviation', 'Conf_sponsors', 'Web_site', 'Begin_date', 'End_date', 'Location', 'Contact', 'Introduction', 'Attendance', 'Detail_paper', 'Important_dates')