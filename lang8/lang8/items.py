# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Lang8Item(Item):
	main = Field()
	correction = Field()
	url = Field()

class CorrectionItem(Item):
	correct = Field()
	incorrect = Field()
