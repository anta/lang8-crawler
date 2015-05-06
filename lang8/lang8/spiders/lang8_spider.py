import scrapy
import re
from scrapy import Selector
from scrapy.http import FormRequest
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from lang8.items import Lang8Item

class Lang8Spider(CrawlSpider):
	name 		= "lang8"
	allowed_domains	= ["lang-8.com"]
	start_urls	= ["http://lang-8.com/1231648/journals"]
	rules = (
			Rule(LinkExtractor(allow=(start_urls[0]+'/',)), callback='parse_item'),
	)

	def start_requests(self):
		yield scrapy.Request('https://lang-8.com/login', callback=self.login)

	def login(self, response):
		formdata = {'username':'','password':''}
		yield FormRequest.from_response(response,
										formnumber=1,
										formdata=formdata,
										clickdata={'name':'commit'},
										callback=self.logged_in)

	def logged_in(self, response):
		yield scrapy.Request(self.start_urls[0])
		#for i in range(1, 1000000, 1):
		#	url = "http://lang-8.com/" + i + "/journals"
		#	yield scrapy.Request(url, callback=self.parse_item)

	def parse_item(self, response):
		self.log('parsing %s' % response.url)
		item = Lang8Item()
		hxs = Selector(response)
		correction_list = hxs.xpath('//div[@class="correction_box"]')
		to_be_remove = ["<p>", "</p>", "<span class=\"f_blue\">", "</span>"]  # words in blue are going to be kept
		to_be_compile = [r"<span class=\"f_red\">(.*?)</span>",
						 r"<span class=\"sline\">(.*?)</span>",
						 r"<span class=\"f_gray\">(.*?)</span>"
						]
		compiled=[]
		for one in to_be_compile:
			compiled.append(re.compile(one))
		if correction_list:
			for co in correction_list:
				correct_xpath = co.xpath('.//li[@class="corrected correct"]')
				if not correct_xpath:
					continue
				incorrect = co.xpath('.//li[@class="incorrect"]/text()').extract()[0]
				correct = correct_xpath.xpath('.//p[1]').extract()[0]
				for one in compiled:
					correct = re.sub(one, "", correct)
				for remove in to_be_remove:
					correct = correct.replace(remove, "")
				self.log('correct=%s\nincorrect=%s' % (correct, incorrect))
		return item
