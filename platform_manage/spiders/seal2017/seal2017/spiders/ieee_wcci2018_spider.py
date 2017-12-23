import scrapy
from ..items import ConferenceInfoItem
from ..date_format import months
import re

class IEEE_WCCI2018(scrapy.Spider):
    name = 'ieee_wcci2018'
    start_urls = [
        'http://www.ecomp.poli.br/~wcci2018/'
    ]

    def parse(self, response):
        conference_item = ConferenceInfoItem()
        conference_item['key_word'] = 'ieee_wcci2018'
        temp_list1 = response.xpath('//section[@id="focus"]//h3/text()').extract()
        temp_list2 = response.xpath('//section[@id="focus"]//p/text()').extract()
        temp_list3 = response.xpath('//section[@id="aboutus"]//p/text()').extract()
        temp_list4 = response.xpath('//section[@id="aboutus"]//ul/li/text()').extract()
        temp_list5 = response.xpath('//section[@id="aboutus"]//ul/li/b/text()').extract()
        temp_str1 = temp_list3[1].split('.')
        temp_str2 = temp_str1[0].split(',')
        temp_str3 = temp_str2[1] + ',' + temp_str2[2]
        temp_str4 = re.compile(r'\d+').findall(temp_list5[5])
        temp_str5 = temp_list5[5].split(' ')
        month = months[temp_str5[0]]
        temp_str6 = temp_list4[5].split(':')
        temp_str7 = temp_list3[0] + '\n' + temp_list1[0] + ',' + temp_list2[0] + '\n' + temp_list1[1] + ',' + temp_list2[1] + '\n' + temp_list1[2] + ',' + temp_list2[2]
        conference_item['conference_name'] = temp_str6[0]
        conference_item['begin_time'] = temp_str4[2] + '-' + month + '-' + temp_str4[0]
        conference_item['end_time'] =temp_str4[2] + '-' + month + '-' + temp_str4[1]
        conference_item['host_address'] = temp_str3.strip()
        conference_item['description'] = temp_str7
        conference_item.save()


