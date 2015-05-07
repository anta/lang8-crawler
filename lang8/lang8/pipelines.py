# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy.exceptions import DropItem

class Lang8Pipeline(object):
	def __init__(self):
		self.file = codecs.open("out.json", "wb", encoding="utf-8")
		self.file.write(u"[")
	def process_item(self, item, spider):
		if not item['correction']:
			raise DropItem("No Correction Scraped in %s" % item['url'])
		line = json.dumps(dict(item)) + ",\n"
		self.file.write(line.decode("unicode_escape"))
		return item
	def close_spider(self, spider):
		self.file.write(u"]")
		self.file.close()
