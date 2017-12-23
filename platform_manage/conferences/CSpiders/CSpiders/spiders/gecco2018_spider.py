import scrapy
from ..items import ConferenceInfoItem
from ..date_format import months
import re

class GECCO2018(scrapy.Spider):
    name = 'gecco2018'
    start_urls = [
        'http://gecco-2018.sigevo.org/index.html/HomePage'
    ]

    def parse(self, response):
        conference_item = ConferenceInfoItem()
        conference_item['key_word'] = 'GECCO2018'
        conference_item['url'] = 'http://gecco-2018.sigevo.org/index.html/HomePage'
        temp_list1 = response.xpath('//section[@id="section_Top"]//h1/text()').extract()
        temp_list2 = response.xpath('//section[@id="section_Top"]//p/text()').extract()
        temp_list3 = response.xpath('//section[@id="section_Top"]//h3/text()').extract()
        temp_list4 = response.xpath('//section[@id="section_Why_gecco"]//p/text()').extract()
        temp_str1 = temp_list1[0]
        temp_str2 = temp_list1[1]
        temp_str3 = temp_list3[0]
        temp_str4 = temp_list2[0]
        temp_str5 = temp_list4[0]
        temp_str6 = re.compile(r'\d+').findall(temp_str3)
        temp_str7 = re.findall(r'@\ (.*)', temp_str1)
        temp_str8 = temp_str3.split(' ')
        month = months[temp_str8[0]]
        conference_item['name'] = temp_str2
        conference_item['begin_time'] = temp_str6[2] + '-' + month + '-' + temp_str6[0]
        conference_item['end_time'] = temp_str6[2] + '-' + month + '-' + temp_str6[1]
        conference_item['host_address'] = temp_str7[0]
        conference_item['description'] = temp_str4 + '\n' + temp_str5
        conference_item.save()


