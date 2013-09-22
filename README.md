Torrents-Crawler
================

This is a scrapy project in which I have implemented several crawlers for different torrent and direct link websites. This project crawls for the title and the url only right now because this was my only requirement.  

###Dependency:
- Scrapy ```pip install scrapy```

###Websites currently supported:
- Piratebay
- Kickass
- 1337x
- SkidrowCrack
- TorrentDownloads
- SumoTorrent
- BitSnoop

###How to run a crawler:
If you want to run a crawler then goto the top level directory which is ```piratebay``` and issue this command:
```$ scrapy crawl piratebay``` (see TODO)
This command will run the piratebay crawler.
Names for all of the crawlers are:
- piratebay
- leetx
- bitsnoop
- sumotorrent
- torrentdownloads
- kickass
- skidrowcrack

###TODO:
Currently I have not added any pipeline so right now if we want to save the crawled data we will have to issue one of the following commands:
- ```scrapy crawl piratebay -o items.json -t json```  
- ```scrapy crawl piratebay -o items.csv -t csv```  
- ```scrapy crawl piratebay -o items.xml -t xml```  
- ```scrapy crawl piratebay -o items.json -t jsonlines```  
If anyone is willing to write an ItemPipeline then feel free to submit a PR

###How to add support:
If you want to add further support for some more websites then feel free to edit this crawler. Just go to ```piratebay/piratebay/spiders/piratebay_spider.py``` and edit that file. Copy one of the class and edit it to adapt for another website. Basically you will have to edit the xpaths, link to .txt file and the name of the crawler. After that copy all of the links which you want to crawl and paste them in a new text file in ```piratebay/links/```. Thats it. After that just run your crawler.

###Author:
- M.Yasoob Ullah Khalid (yasoob.khld@gmail.com)

###Support:
[Official scrapy docs](http://doc.scrapy.org/en/latest/intro/tutorial.html)
If there is an issue with the scripts present here do open an issue or if you want me to add support for a website do tell me.

###Contribute:
You can contribute literraly anything. Whether a new crawler or some small optimisations. Just do a PR and make this project grow.
