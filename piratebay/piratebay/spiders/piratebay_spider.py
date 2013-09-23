from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

import urllib
import urlparse

from piratebay.items import UniversalItem

class PiratebaySpider(BaseSpider):
    name = "piratebay"
    allowed_domains = ["thepiratebay.sx"]
    with open('links/piratebay.txt', 'r') as file:
        start_urls = [i.strip() for i in file.readlines()]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@class="detName"]')
        for site in sites:
            item = UniversalItem()
            item['title'] = site.select('a/text()').extract()[0]
            item['link'] = "http://thepiratebay.sx" + site.select('a/@href').extract()[0]
            item['ref'] = "thepiratebay.sx"
            yield item

class KickassSpider(BaseSpider):
    name = "kickass"
    allowed_domains = ["kickass.io"]
    with open('links/kickass.txt', 'r') as file:
        start_urls = [i.strip() for i in file.readlines()]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@class="torrentname"]')
        for site in sites:
            item = UniversalItem()
            item['title'] = site.select('a[2]/text()').extract()[0]
            item['link'] = "http://kickass.to" + site.select('a/@href').extract()[0]
            item['ref'] = "kickass.io"
            yield item

class LeetxSpider(BaseSpider):
    name = "leetx"
    allowed_domains = ["1337x.org"]
    with open('links/leetx.txt', 'r') as file:
        start_urls = [i.strip() for i in file.readlines()]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//h3[@class="org"]')
        for site in sites:
            item = UniversalItem()
            item['title'] = site.select('a/text()').extract()[0]
            item['link'] = "http://1337x.org" + site.select('a/@href').extract()[0]
            item['ref'] = "1337x.org"
            yield item

class SkidrowCrackSpider(BaseSpider):
    name = "skidrowcrack"
    allowed_domains = ["skidrowcrack.com"]
    with open('links/skidrowcrack.txt', 'r') as file:
        start_urls = [i.strip() for i in file.readlines()]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul[@class="lcp_catlist"]/li')
        for site in sites:
            item = UniversalItem()
            item['title'] = site.select('a/text()').extract()[0]
            item['link'] = site.select('a/@href').extract()[0]
            item['ref'] = "skidrowcrack.com"
            yield item

class TorrentDownloadsSpider(BaseSpider):
    name = "torrentdownloads"
    allowed_domains = ["torrentdownloads.me"]
    with open('links/torrentdownloads.txt', 'r') as file:
        start_urls = [i.strip() for i in file.readlines()]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//div[@class="inner_container"]/div/p/a/text()').extract()
        links = hxs.select('//div[@class="inner_container"]/div/p/a/@href').extract()
        for i, v in zip(titles,links):
            item = UniversalItem()
            item['title'] = i
            item['link'] = "http://www.torrentdownloads.me" + v
            item['ref'] = "torrentdownloads.me"
            yield item

class SumoTorrentSpider(BaseSpider):
    name = "sumotorrent"
    allowed_domains = ["sumotorrent.sx"]
    with open('links/sumotorrent.txt', 'r') as file:
        start_urls = [i.strip() for i in file.readlines()]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@style="overflow:hidden;width:95%;height:15px;padding-top:4px;padding-bottom:4px;white-space: nowrap;"]')
        for site in sites:
            item = UniversalItem()
            item['title'] = site.select('a/text()').extract()[0]
            item['link'] = url_fix(site.select('a/@href').extract()[0])
            item['ref'] = "sumotorrent.sx"
            yield item

class BitSnoopSpider(BaseSpider):
    name = "bitsnoop"
    allowed_domains = ["bitsnoop.com"]
    start_urls = ["http://bitsnoop.com/popular/seeders_games.html"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ol[@id="torrents"]/li')
        for site in sites:
            item = UniversalItem()
            item['title'] = site.select('a/text()').extract()[0]
            item['link'] = "http://bitsnoop.com" + url_fix(site.select('a/@href').extract()[0])
            item['ref'] = "bitsnoop.com"
            yield item

def url_fix(s, charset='utf-8'):
    if isinstance(s, unicode):
        s = s.encode(charset, 'ignore')
    scheme, netloc, path, qs, anchor = urlparse.urlsplit(s)
    path = urllib.quote(path, '/%')
    qs = urllib.quote_plus(qs, ':&=')
    return urlparse.urlunsplit((scheme, netloc, path, qs, anchor))
