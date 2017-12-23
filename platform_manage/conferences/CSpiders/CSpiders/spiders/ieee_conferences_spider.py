import scrapy
from ..items import ConferenceInfoItem
from ..date_format import months
import re

class IEEE_CONFERENCES(scrapy.Spider):
    name = 'ieee_conferences'
    allowed_domains = ['ieee.org']
    start_urls = [
        'https://www.ieee.org/conferences_events/conferences/search/conference_search_results.html?WT.mc_id=lp_con_search'
    ]

    def parse(self, response):
        #yield scrapy.Request(response.url,callback=self.parse_pg)
        next_list1 = response.css('div.pagination a::attr(href)').extract()
        url_temp1 = next_list1[-1]
        RowsPerPage = re.findall(r'RowsPerPage=(.\d+)',next_list1[-1])[0]
        Max_Activepage = re.findall(r'ActivePage=(.\d+)',next_list1[-1])[0]
        # for i in range(1,int(Max_Activepage)+1):
        for i in range(1,3):
            url_temp2 = re.sub(r'ActivePage=(.\d+)*', 'ActivePage=' + str(i), url_temp1)
            url_temp3 = re.sub(r'ROWSTART=(.\d+)*', 'ROWSTART=' + str((i - 1) * int(RowsPerPage)), url_temp2)
            next_pageUrl = 'https://www.ieee.org' + url_temp3
            # print(next_pageUrl)
            yield scrapy.Request(next_pageUrl,callback=self.parse_pg)

    def parse_pg(self,response):
        # print(response.url,'\n')
        # print('parse_pg','\n')
        url_lists1 = response.css('table.nogrid-nopad td.pad10 a::attr(href)').extract()
        detail_url = sorted(set(url_lists1), key=url_lists1.index)
        for url in detail_url:
            conference_url = 'https://www.ieee.org'+url
            yield scrapy.Request(conference_url,callback=self.parse_detail)

    def parse_detail(self,response):
        item = ConferenceInfoItem()
        name = response.css('div.box-lc-top-indent a::text').extract()[0]
        sponsors_list = response.css('div.box-lc-top-indent li::text').extract()
        sponsors = ''
        for i in sponsors_list:
            sponsors += i.strip() + ';'
        intro = response.css('div.box-lc-top-indent div.content-262 p::text').extract()[0]
        patt = re.compile(r"\((.*?)\)", re.I | re.X)
        try:
            abbr = patt.findall(name)[0]
        except:
            abbr = ''
        if abbr == '':
            try:
                abbr = patt.findall(intro)[0]
            except:
                abbr = ''
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
        for index, val in enumerate(temp_list2):
            if val == 'Dates':
                temp_list = temp_list1[index].css('p::text').extract()
                date_list = temp_list[0].split(' ')
                month1 = months[date_list[1]]
                month2 = months[date_list[4]]
                begin_date = date_list[5] + '-' + month1 + '-' + date_list[0]
                end_date = date_list[5] + '-' + month2 + '-' + date_list[3]
                # print(begin_date,'\n',end_date)
            if val == 'Location':
                temp_list = temp_list1[index].css('p::text').extract()
                location = ''
                for list in temp_list:
                    if list.strip() == '':
                        continue
                    location += list.strip() + ';'
                    # print(location)
            if val == 'Contact':
                temp_list = temp_list1[index].css('p::text').extract()
                contact = ''
                for list in temp_list:
                    if list.strip() == '':
                        continue
                    contact += list.strip() + ';'
                    # print(contact)
            if val == 'Web site':
                web_site = temp_list1[index].css('p a::attr(href)').extract()[0]
                # print(web_site)
            if val == 'Conference #':
                conf_id = temp_list1[index].css('p::text').extract()[0]
                # print(conf_id)
            if val == 'Attendance':
                attendance = temp_list1[index].css('p::text').extract()[0]
                # print(attendance)
            if val == 'Call for Papers for Conference Authors':
                temp_list = response.xpath(
                    '//div[@class="content-2col-r"]//div[@class="div-pad5b"]//p/text()').extract()
                detail_paper = ''
                important_date = ''
                try:
                    a_text = \
                    response.xpath('//div[@class="content-2col-r"]//div[@class="div-pad5b"]//a/text()').extract()[0]
                    if a_text == 'View call for papers':
                        detail_paper = response.css('div.content-2col-r div.div-pad5b a::attr(href)').extract()[0]
                    try:
                        for list in temp_list:
                            important_date += list.strip() + ';'
                    except:
                        important_date = ''
                except:
                    pass
                try:
                    if temp_list[0] == 'No call for papers available at this me.':
                        detail_paper = ''
                    try:
                        important_date = ''
                        for index, list in enumerate(temp_list):
                            if index == 0:
                                continue
                            important_date += list.strip() + ';'
                    except:
                        important_date = ''
                except:
                    pass
                # print(detail_paper,'\n',important_date)

        item['Conf_name'] = name
        item['Crawl_url'] = response.url
        item['Conf_ID'] = conf_id
        item['Abbreviation'] = abbr
        item['Conf_sponsors'] = sponsors
        item['Web_site'] = web_site
        item['Begin_date'] = begin_date
        item['End_date'] = end_date
        item['Location'] = location
        item['Contact'] = contact
        item['Introduction'] = intro
        item['Attendance'] = attendance
        item['Detail_paper'] = detail_paper
        item['Important_dates'] = important_date
        item.save()





