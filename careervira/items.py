# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CareerviraItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    ShortDescription =scrapy.Field()
    Description =scrapy.Field()
    Keyskills =scrapy.Field()
    Prerequitsites =scrapy.Field()
    Syllabus =scrapy.Field()
    Price =scrapy.Field()

