import scrapy
from ..items import ConferenceInfoItem
from ..date_format import months
import re

class IEEE_CONFERENCES(scrapy.Spider):
    name = 'test_ieee'
    allowed_domains = ['ieee.org']
    start_urls = [
        'https://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=38163'
        #'https://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=42644'
        #'https://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=40311'
        #'https://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=43071'
    ]

    def parse(self, response):
        item = ConferenceInfoItem()
        name = response.css('div.box-lc-top-indent a::text').extract()[0]
        sponsors_list = response.css('div.box-lc-top-indent li::text').extract()
        sponsors = ''
        for i in sponsors_list:
            sponsors += i.strip()+';'
        intro = response.css('div.box-lc-top-indent div.content-262 p::text').extract()[0]
        #key_word = re.findall(r'[^()]',intro)
        print(intro,'\n')
        patt = re.compile(r"\((.*?)\)", re.I|re.X)
        try:
            key_word = patt.findall(name)
        except:
            key_word = ''
        if key_word == '':
            try:
                key_word = patt.findall(intro)
            except:
                key_word = ''
        print(key_word,'\n')
        # print(name,'\n',sponsors,'\n',intro,'\n')

        temp_list1 = response.css('div.box-lc-indent div.content-101-10-right-nowrap')
        temp_list2 = response.css('div.box-lc-indent h4::text').extract()
        conf_id = ''
        web_site = ''
        begin_date = ''
        end_date = ''
        location = ''
        contact = ''
        attendance = ''
        detail_paper = ''
        important_date = ''
        for index,val in enumerate(temp_list2):
            if val == 'Dates':
                temp_list = temp_list1[index].css('p::text').extract()
                date_list = temp_list[0].split(' ')
                month1 = months[date_list[1]]
                month2 = months[date_list[4]]
                begin_date = date_list[5]+'-'+month1+'-'+date_list[0]
                end_date = date_list[5] + '-' + month2 + '-' + date_list[3]
                #print(begin_date,'\n',end_date)
            if val == 'Location':
                temp_list = temp_list1[index].css('p::text').extract()
                location = ''
                for list in temp_list:
                    if list.strip() == '':
                        continue
                    location += list.strip()+';'
                #print(location)
            if val == 'Contact':
                temp_list = temp_list1[index].css('p::text').extract()
                contact = ''
                for list in temp_list:
                    if list.strip() == '':
                        continue
                    contact += list.strip() + ';'
                #print(contact)
            if val == 'Web site':
                web_site = temp_list1[index].css('p a::attr(href)').extract()[0]
                #print(web_site)
            if val == 'Conference #':
                conf_id = temp_list1[index].css('p::text').extract()[0]
                #print(conf_id)
            if val == 'Attendance':
                attendance = temp_list1[index].css('p::text').extract()[0]
                #print(attendance)
            if val == 'Call for Papers for Conference Authors':
                temp_list = response.xpath('//div[@class="content-2col-r"]//div[@class="div-pad5b"]//p/text()').extract()
                detail_paper = ''
                important_date = ''
                try:
                    a_text = response.xpath('//div[@class="content-2col-r"]//div[@class="div-pad5b"]//a/text()').extract()[0]
                    if a_text == 'View call for papers':
                        detail_paper = response.css('div.content-2col-r div.div-pad5b a::attr(href)').extract()[0]
                    try:
                        for list in temp_list:
                            important_date += list.strip() + ';'
                    except:
                        important_date = ''
                except:
                    print('Information error!')
                try:
                    if temp_list[0] == 'No call for papers available at this me.':
                        detail_paper = ''
                    try:
                        important_date = ''
                        for index,list in enumerate(temp_list):
                            if index == 0:
                                continue
                            important_date += list.strip() + ';'
                    except:
                        important_date = ''
                except:
                    print('Information error!')
                #print(detail_paper,'\n',important_date)






