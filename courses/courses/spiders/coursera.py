# -*- coding: utf-8 -*-
import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'coursera'
    allowed_domains = ['https://pt.coursera.org/browse?languages=pt']
    start_urls = ['https://pt.coursera.org/browse?languages=pt/']

    def parse(self, response):
        self.log('Hello World!  Scrapy Project #######################################3')
