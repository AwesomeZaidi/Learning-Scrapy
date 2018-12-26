# Learning-Scrapy
https://doc.scrapy.org/en/latest/intro/tutorial.html
This tutorial will walk you through these tasks:
 - Creating a new Scrapy project
 - Writing a spider to crawl a site and extract data
 - Exporting the scraped data using the command line
 - Changing spider to recursively follow links
 - Using spider arguments


### What's a Spider?
https://doc.scrapy.org/en/latest/topics/spiders.html#topics-spiders
Spiders are classes which define how a certain site (or a group of sites) will be scraped, including how to perform the crawl (i.e. follow links) and how to extract structured data from their pages (i.e. scraping items). In other words, Spiders are the place where you define the custom behaviour for crawling and parsing pages for a particular site (or, in some cases, a group of sites).

For spiders, the scraping cycle goes through something like this:

You start by generating the initial Requests to crawl the first URLs, and specify a callback function to be called with the response downloaded from those requests.

The first requests to perform are obtained by calling the start_requests() method which (by default) generates Request for the URLs specified in the start_urls and the parse method as callback function for the Requests.

In the callback function, you parse the response (web page) and return either dicts with extracted data, Item objects, Request objects, or an iterable of these objects. Those Requests will also contain a callback (maybe the same) and will then be downloaded by Scrapy and then their response handled by the specified callback.

In callback functions, you parse the page contents, typically using Selectors (but you can also use BeautifulSoup, lxml or whatever mechanism you prefer) and generate items with the parsed data.

Finally, the items returned from the spider will be typically persisted to a database (in some Item Pipeline) or written to a file using Feed exports.

Even though this cycle applies (more or less) to any kind of spider, there are different kinds of default spiders bundled into Scrapy for different purposes. We will talk about those types here.

### Project Structure
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py

## How to run our spider
To put our spider to work, go to the project’s top level directory and run:
`scrapy crawl quotes`

`scrapy shell url` downloads the page from the url we just passed and provides us with a response object that we can use to access the data from the page. For example, `print(response.text)` gives us the whole page content.

We can use the response.css('selector') method to return the elements matched by this selector. This at a basic implementation will return the Selector object inside. We can use the `extract()` method on such an object to get the actual HTML data we selected. To get rid of the HTML tags, after the selector name within the qoutes we add a double colon text `::text` and we want just a string not a list so we can target `[0].extract()` or even better, `.extract_first() which will return None if nothing is found instead of throwing an error.`

https://code.tutsplus.com/tutorials/the-30-css-selectors-you-must-memorize--net-16048