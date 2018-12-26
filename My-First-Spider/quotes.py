# -*- coding: utf-8 -*-
# import scrapy


# Understand what a sub class does again?
# class MultipleQuotesPaginationSpider(scrapy.Spider):
#     name = 'multiple-quotes-pagination'
#     allowed_domains = ['toscrape.com']
#     start_urls = ['http://quotes.toscrape.com']

#     # this method is where our Spider will extract the data.
#     # to do this, it has to generate one or many dictionaries.
#     def parse(self, response):
#         self.log('I just visited: ' + response.url)
#         for quote in response.css('div.quote'):
#             item = {
#                 'author_name': response.css('small.author::text').extract_first(),
#                 'text': response.css('span.text::text').extract_first(),
#                 'tags': response.css('a.tag::text').extract(),
#             }
#             yield item #for every page, parse method will extract the data
#         # Next, we find the url to the next page, then create a request for this new page.
#         # this will repeat till there are no more quotes in this website. 
#         next_page_url = response.css('li.next > a::attr(href)').extract_first()
#         if next_page_url:
#             # follow pagination link 
#             next_page_url = response.urljoin(next_page_url)
#             yield Scrapy.Request(url = next_page_url, callback = self.parse)


# -*- coding: utf-8 -*-
import scrapy


class MultipleQuotesPaginationSpider(scrapy.Spider):
    name = "multiple-quotes-pagination"
    allowed_domains = ["toscrape.com"]
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        for quote in response.css('div.quote'):
            item = {
                'author_name': quote.css('small.author::text').extract_first(),
                'text': quote.css('span.text::text').extract_first(),
                'tags': quote.css('a.tag::text').extract(),
            }
            yield item
        # follow pagination link
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)