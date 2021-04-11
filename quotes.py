import scrapy
import re
from scrapy_splash import SplashRequest 

class QuotesSpider(scrapy.Spider):
    name = 'quotesjs'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/js/']
    
    ### Starts requests by sending URLs in start_urls for splash to render - The rendered content is then sent to a callback function (parse)
    def start_requests(self): 
        for url in self.start_urls: 
            yield SplashRequest(url, self.parse, 
                endpoint='render.html', 
                args={'wait': 1}, 
           )
    
    ### The actual gathering of content is not different from the usual scrapy method
    ### Actually, the only thing that changes is how the requests are sent and retrieved - They pass through the Splash middleware
    ### This function will get text, author and tags info for each quote and yield it
    ### If the next page element is present, it will yield another request to Splash, which will then be processed by the parse function again
    def parse(self, response): 
        next_page = str(response.css('.next > a::attr(href)').extract_first())

        for quote in response.css('.quote'):
            yield {
                'text' : re.sub("“|”", '', (quote.css('.text::text').extract_first())), ### This cleans the ending/starting quotes using regex
                'author' : quote.css('small.author::text').extract(),
                'tags' : ', '.join(quote.css('a.tag::text').extract())
            }
        
        if next_page:
            yield SplashRequest(response.urljoin(next_page), self.parse, 
            endpoint='render.html', 
            args={'wait': 1}, 
            )
