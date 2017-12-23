from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from .CSpiders.CSpiders.spiders.seal2017_spider import SEAL2017
from .CSpiders.CSpiders.spiders.gecco2017_spider import GECCO2017
from .CSpiders.CSpiders.spiders.gecco2018_spider import GECCO2018
from .CSpiders.CSpiders.spiders.ieee_wcci2018_spider import IEEE_WCCI2018

class RunSpiders():
    '''
    runner = CrawlerRunner()
    runner.crawl(SEAL2017)
    runner.crawl(GECCO2017)
    runner.crawl(GECCO2018)
    runner.crawl(IEEE_WCCI2018)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run(installSignalHandlers=False)
    '''
