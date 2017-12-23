# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from spiders.models import ConferenceInfo
from scrapy_djangoitem import DjangoItem

class Seal2017Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ConferenceInfoItem(DjangoItem):
    django_model = ConferenceInfo
