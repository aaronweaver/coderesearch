import scrapy
from scrapy.selector import Selector

class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['http://stackoverflow.com/questions/tagged/python']

    def parse(self, response):
        #Parse out the URL's to request
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            print full_url
            #print "***"
            #print response.css
            #print "***"
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):

        rep =  response.css('.accepted-answer')

        #To Do: Parse out the code tags
        #yield {
        #    'title': response.css('h1 a::text').extract()[0],
        #    'votes': response.css('.question .vote-count-post::text').extract()[0],
        #    'body': response.css('.question .post-text').extract()[0],
        #    'tags': response.css('.question .post-tag::text').extract(),
        #    'link': response.url,
        #}
        #scrapy shell http://stackoverflow.com/questions/509211/explain-pythons-slice-notation
