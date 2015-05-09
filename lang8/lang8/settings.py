# -*- coding: utf-8 -*-

# Scrapy settings for lang8 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lang8'

SPIDER_MODULES = ['lang8.spiders']
NEWSPIDER_MODULE = 'lang8.spiders'
ITEM_PIPELINES = {'lang8.pipelines.Lang8Pipeline':'123'}
COOKIE_ENABLED = False
DOWNLOAD_DELAY = 3
RETRY_TIMES = 200
#LOG_FILE = 'lang8.log'
LOG_LEVEL = 'DEBUG'
LOG_ENCODING = 'utf-8'
USER_AGENT_LIST = [
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
		'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
]
HTTP_PROXY = 'http://127.0.0.1:8123'
DOWNLOADER_MIDDLEWARES = {
		'lang8.middlewares.RandomUserAgentMiddleware': 400,
		'lang8.middlewares.ProxyMiddleware': 410,
		'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lang8 (+http://www.yourdomain.com)'
