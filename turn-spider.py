from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from demoscrapy.demoscrapy.spiders.demospider import DemospiderSpider


process = CrawlerProcess(get_project_settings())
process.crawl(DemospiderSpider)
process.start()
