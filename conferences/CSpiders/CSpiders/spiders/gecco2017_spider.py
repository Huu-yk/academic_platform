import scrapy
from ..items import ConferenceInfoItem
from ..date_format import months
import re

class GECCO2017(scrapy.Spider):
    name = 'gecco2017'
    start_urls = [
        'http://gecco-2017.sigevo.org/index.html/HomePage'
    ]

    def parse(self, response):
        conference_item = ConferenceInfoItem()
        conference_item['key_word'] = 'GECCO2017'
        conference_item['url'] = 'http://gecco-2017.sigevo.org/index.html/HomePage'
        lists = response.xpath('//div[@class="text-center"]')
        temp_list1 = lists[0].xpath('//h1')
        temp_str1 = temp_list1[1].xpath('text()').extract()[0]
        temp_str2 = temp_list1[2].xpath('text()').extract()[0]
        temp_str3 = lists[0].xpath('//h3/text()').extract()[0]
        temp_str4 = lists[0].xpath('//p/text()').extract()[0]
        temp_str5 = lists[0].xpath('//p/text()').extract()[1]
        temp_str6 = re.compile(r'\d+').findall(temp_str3)
        temp_str7 = re.findall(r'@\ (.*)',temp_str1)
        temp_str8 = temp_str3.split(' ')
        month = months[temp_str8[0]]
        conference_item['name'] = temp_str2
        conference_item['begin_time'] = temp_str6[2] + '-' + month + '-' + temp_str6[0]
        conference_item['end_time'] =temp_str6[2] + '-' + month + '-' + temp_str6[1]
        conference_item['host_address'] = temp_str7[0]
        conference_item['description'] = temp_str4 + '\n' + temp_str5
        conference_item.save()