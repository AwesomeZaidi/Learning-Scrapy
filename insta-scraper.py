# -*- coding: utf-8 -*-
import scrapy

class InstaSpider(scrapy.Spider):
    name = 'insta-spider'
    login_url = 'https://www.instagram.com/accounts/login/'
    start_urls = [login_url]

    custom_settings = {
        'USER_AGENT': 'asims-cool-project (http://instagram.com)',
    }
    def parse(self, response):
        # extract the csrf token value
        # can't find this token in the instagram source code exactly. It does exist in their inline script but not how we grabbed it from the quotes login form.
        # token = response.css('input[name="csrf_token"]::attr(value)').extract_first()
        # create a python dictionary with the form values
        data = {
            'username': '',
            'password': '',
        }
        # submit a POST request to it
        yield scrapy.FormRequest(url=self.login_url, formdata=data, callback=self.parse_quotes)

    def parse_quotes(self, response):
        """Parse the main page after the spider is logged in"""
        print("PARSING INFO, INSIDE LOGIN.")
        # for q in response.css('div.quote'):
        #     yield {
        #         'author_name': q.css('small.author::text').extract_first(),
        #         'author_url': q.css(
        #             'small.author ~ a[href*="goodreads.com"]::attr(href)'
        #         ).extract_first()
        #     }