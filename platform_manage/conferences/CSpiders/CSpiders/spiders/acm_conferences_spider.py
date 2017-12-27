import scrapy
from ..items import ConferenceInfoItem
from ..date_format import months
import re
from queue import Queue

class ACM_CONFERENCES(scrapy.Spider):
    name = 'acm_conferences'
    start_urls = [
        'https://www.acm.org/conferences'
    ]

    def parse(self, response):
        href_list = response.xpath('//ul[@class="show-hide"]//a/@href').extract()
        text_list = response.xpath('//ul[@class="show-hide"]//a/text()').extract()
        p_list = response.xpath('//ul[@class="show-hide"]//p/text()').extract()
        time_list = response.xpath('//ul[@class="show-hide"]//time/text()').extract()
        hq = Queue()
        tq = Queue()
        pq = Queue()
        tbq = Queue()
        teq = Queue()
        for h in href_list:
            hq.put(h.strip())
            # print(h.strip())
        for t in text_list:
            tq.put(t.strip())
            # print(t.strip())
        for p in p_list:
            pq.put(p.strip())
            # print(p.strip())
        for time in time_list:
            dates = "".join(time.split())
            temp_str1 = re.compile(r'\d+').findall(dates)
            m1 = dates[0:3]
            m2 = dates[6:9]
            begin_date = temp_str1[2] + '-' + months[m1] + '-' +temp_str1[0]
            end_date = temp_str1[2] + '-' + months[m2] + '-' + temp_str1[1]
            tbq.put(begin_date)
            teq.put(end_date)
            # print(begin_date,end_date)

        while not tq.empty():
            yield self.saveData(tq.get(),hq.get(),pq.get(),tbq.get(),teq.get())

    def saveData(self,name,site,location,begin,end):
        item = ConferenceInfoItem()
        item['Conf_name'] = name
        item['Web_site'] = site
        item['Location'] = locatio长度n
        item['Begin_date'] = begin
        item['End_date'] = end
        item['Crawl_url'] = 'https://www.acm.org/conferences'
        item.save()