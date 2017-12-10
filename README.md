# Lang8 Crawler
## Overview

Lang8 Crawler written in Python is based on scrapy, a fast high-level web crawling and web scraping framework. For more information about scrapy, check the homepage at: http://scrapy.org/

#### The following features included
* Tor and Polipo support to create anonymous crawler and avoid being banned
* Crawl each journal for each user on Lang8 and corresponding correct/incorrect pairs
* Unicode support
* Output JSON format

## Requirements
* Python 2.7
* Works on Linux, Windows, Mac OSX, BSD
* Tor (optional feature)
* Polipo (optional feature)

## Installation
You can disable Tor and Polipo support in settings.py to skip step 3 and 4

* Install Python 2.7
* Install [Scrapy](http://doc.scrapy.org/en/latest/intro/install.html)
* Install [Tor](https://www.torproject.org/)
* Install [Polipo](http://www.pps.univ-paris-diderot.fr/~jch/software/polipo/) and edit polipo config file as follows
```
socksParentProxy = localhost:9050
diskCacheRoot=""
disableLocalInterface=""
```
* Run polipo via `polipo -c CONFIG_FILE daemonise=true logFile=LOG_FILE`
* change directory to lang8-crawler/lang8 and run Lang8 Crawler via `scrapy crawl lang8`

## Configuration
* Modify the lang8-crawler/lang8/lang8/settings.py to config scrapy. Check the self-explainable comments in settings.py 
