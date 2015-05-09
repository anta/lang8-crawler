#Lang8 Crawler
##Overview

Lang8 Crawler written in Python is based on scrapy, a fast high-level web crawling and web scraping framework. For more information about scrapy, check the homepage at: http://scrapy.org/

####The following features included
* Tor and Polipo support to create anonymous crawler and avoid being banned
* Crawl each journal for each user on Lang8 and corresponding correct/incorrect pairs
* Unicode support
* Output JSON format

##Requirements
* Python 2.7
* Works on Linux, Windows, Mac OSX, BSD
* Tor (optional feature)
* Polipo (optional feature)

##Installation
1. Install Python
2. Install Scrapy
3. Install Tor
4. Install Polipo and edit polipo config file as follows

```
socksParentProxy = localhost:9050
diskCacheRoot=""<br>
disableLocalInterface=""<br>
```
