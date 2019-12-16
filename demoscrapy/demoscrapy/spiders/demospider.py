from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DemospiderSpider(CrawlSpider):
    handle_httpstatus_list = [403, 404]
    name = 'demospider'
    allowed_domains = ['mydomain.com']
    start_urls = ['http://mydomain.com/']
    custom_settings = {
    'LOG_FILE': 'logs/demospider.log',
    'LOG_LEVEL': 'DEBUG'
    }

    rules = (
    Rule(
      LinkExtractor(
        tags='a',
        attrs='href',
        unique=True
      ),
      callback='parse_item',
      follow=True
    ),
    )

    def parse_item(self, response):
        pass
