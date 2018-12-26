## Creating our first Spider
`scrapy genspider quotes toscrape.com`
- the first parameter here 'quotes' is the name of our spider which is usually named after the site we're scraping.
- the second parameter here is the domain of the site we want to scrape.
This command will generate a Spider. 

## How to run Spider?
`scrapy runspider quotes.py`
- This will print a lot of info about the execution. 

## How to save data into a file
concatenate the run command with `-o filename.ext`
run `more filename.ext` to view the data in terminal