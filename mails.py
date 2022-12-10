import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MailsSpider(CrawlSpider):
    name = 'mails'
    allowed_domains = ['www.zoho.com']
    start_urls = ['https://www.zoho.com']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        emails = re.findall(r'[\w\.]+@[\w\.]+', response.text)
        print(emails)
