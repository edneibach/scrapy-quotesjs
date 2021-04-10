# scrapy-quotesjs
This is a sample spider based on scrapy and splash. 

Its purpose is to scrape quotes.toscrape.com/js/, which uses javascript to render its content - Thus, not being scrapable by scrapy only.

It sends a request for Splash to render the page content and return it to scrapy, which will then parse its content.

You will need to have scrapy and splash for python installed. You will also need to have access to an instance of Splash, either running in docker locally or through an external IP, which should be configured in the settings.py file.
