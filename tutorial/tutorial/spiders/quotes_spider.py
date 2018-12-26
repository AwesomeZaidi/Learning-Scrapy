import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # must return an iterable of Requests that the spider will begin to crawl from.
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # handles the response of each request downloaded.
    # The response parameter is an instance of TextResponse
    # that holds the page content and has further helpful methods to handle it.
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)