""" 
I tried to modify the code from class to get link titles from the nature.com website, but the result was not what I expected based on the example. I was able to successfully get other content from the lego site, but my attempts to get data from several other websites have failed. Wanna give me a hint? 
Here is some code that I would expect to work:
"""


import scrapy

class natureSpider(scrapy.Spider):
    name = "nature_spider"
    start_urls = ['http://www.nature.com/news/']
    
    def parse(self, response):
        SET_SELECTOR = '.set'
        for nat in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h3 a ::text'
            yield {
                'name': nat.css(NAME_SELECTOR).extract_first(),
            }
###############################

"""
And a sample of the html that I was expecting to be able to extract from:

<h3><span class="article-type">Trend watch</span><a href="http://www.nature.com/news/ebola-funding-surge-hides-falling-investment-in-other-neglected-diseases-1.21505">Ebola funding surge hides falling investment in other neglected diseases</a></h3>
"""
