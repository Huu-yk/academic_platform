'''
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from .spiders import seal2017_spider
from .spiders import gecco_spider

runner = CrawlerRunner()
runner.crawl(gecco_spider.Gecco)
runner.crawl(seal2017_spider.Seal2017)
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()
'''