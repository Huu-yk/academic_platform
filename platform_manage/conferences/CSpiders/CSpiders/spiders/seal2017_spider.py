import scrapy
from ..items import ConferenceInfoItem
from ..date_format import months

class SEAL2017(scrapy.Spider):
    name = 'seal2017'
    start_urls = [
        'http://www.seal2017.com/'
    ]

    def parse(self, response):
        conference_item = ConferenceInfoItem()
        conference_item['key_word'] = 'SEAL2017'

        lists = response.css('#date_ribbon span')
        conference_item['name'] = lists[0].xpath('text()').extract()[0]
        conference_item['url'] = 'http://www.seal2017.com/'
        temp_str1 = lists[1].xpath('text()').extract()[0].split(',')
        temp_str2 = temp_str1[0].strip().split(' ')
        month = months[temp_str2[0]]
        temp_days = temp_str2[1].split('-')

        conference_item['begin_time'] = temp_str1[1].strip() + '-' + month + '-' + temp_days[0]
        conference_item['end_time'] = temp_str1[1].strip() + '-' + month + '-' + temp_days[1]

        more_info = response.xpath("//div[@class='col-md-4']/p")
        temp_str3 = more_info[0].xpath('a/text()').extract_first()

        conference_item['host_address'] = temp_str1[2].strip() + ', ' + temp_str1[3].strip() + ', ' + temp_str3

        temp_str4 = more_info[1].xpath('text()').extract()[0].strip()
        temp_str4 = temp_str4.replace('\n', '')
        temp_str4 = temp_str4.replace('  ', '')
        conference_item['description'] = temp_str4.strip()
        conference_item.save()
