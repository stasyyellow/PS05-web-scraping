# PS05-web-scraping
 scrapy




выполнение: 
`PS C:\_Python AI\github\PS05-web-scraping> cd "C:\_Python AI\github\PS05-web-scraping\divanpars"`
`PS C:\_Python AI\github\PS05-web-scraping\divanpars> python -m scrapy crawl lighting`
2024-08-28 12:50:30 [scrapy.utils.log] INFO: Scrapy 2.11.2 started (bot: divanpars)
2024-08-28 12:50:33 [scrapy.utils.log] INFO: Versions: lxml 5.2.2.0, libxml2 2.11.7, cssselect 1.2.0, parsel 1.9.1, w3lib 2.2.1, Twisted 24.3.0, Python 3.12.5 (tag
s/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)], pyOpenSSL 24.1.0 (OpenSSL 3.2.2 4 Jun 2024), cryptography 42.0.8, Platform Windows-10-10.0.19045-SP0
2024-08-28 12:50:33 [scrapy.addons] INFO: Enabled addons:
[]
2024-08-28 12:50:33 [asyncio] DEBUG: Using selector: SelectSelector
2024-08-28 12:50:33 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.asyncioreactor.AsyncioSelectorReactor
2024-08-28 12:50:33 [scrapy.utils.log] DEBUG: Using asyncio event loop: asyncio.windows_events._WindowsSelectorEventLoop
2024-08-28 12:50:34 [scrapy.extensions.telnet] INFO: Telnet Password: c2c1f4f06bb38e29
2024-08-28 12:50:38 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']
2024-08-28 12:50:38 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'divanpars',
 'FEED_EXPORT_ENCODING': 'utf-8',
 'NEWSPIDER_MODULE': 'divanpars.spiders',
 'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['divanpars.spiders'],
 'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'}
2024-08-28 12:50:50 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2024-08-28 12:50:51 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2024-08-28 12:50:51 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2024-08-28 12:50:51 [scrapy.core.engine] INFO: Spider opened
2024-08-28 12:50:51 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2024-08-28 12:50:51 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2024-08-28 12:50:52 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/robots.txt> (referer: None)
2024-08-28 12:50:53 [urllib3.connectionpool] DEBUG: Starting new HTTPS connection (1): publicsuffix.org:443
2024-08-28 12:50:55 [urllib3.connectionpool] DEBUG: https://publicsuffix.org:443 "GET /list/public_suffix_list.dat HTTP/1.1" 200 86877
2024-08-28 12:50:55 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/category/svet> (referer: None)
2024-08-28 12:50:56 [lighting] INFO: Обработка URL: https://www.divan.ru/category/svet
2024-08-28 12:50:56 [lighting] INFO: Количество найденных URL продуктов: 192
2024-08-28 12:50:56 [scrapy.dupefilters] DEBUG: Filtered duplicate request: <GET https://www.divan.ru/product/podvesnoj-svetilnik-sanset-black> - no more duplicates will be shown (see DUPEFILTER_DEBUG to show all duplicates)
2024-08-28 12:50:56 [lighting] INFO: Следующая страница не найдена.
2024-08-28 12:50:57 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/bra-vario-white> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:57 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-sanset-black> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:57 [lighting] DEBUG: Извлеченные данные продукта: Бра Варио White - 990
2024-08-28 12:50:57 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/bra-vario-white>
{'name': 'Бра Варио White', 'price': '990', 'link': 'https://www.divan.ru/product/bra-vario-white'}
2024-08-28 12:50:57 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Сансет Black - 5190
2024-08-28 12:50:57 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-sanset-black>
{'name': 'Подвесной светильник Сансет Black', 'price': '5190', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-sanset-black'}
2024-08-28 12:50:57 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/bra-babl-black> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:57 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-babl-3> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:57 [lighting] DEBUG: Извлеченные данные продукта: Бра Бабл Black - 1990
2024-08-28 12:50:57 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/bra-babl-black>
{'name': 'Бра Бабл Black', 'price': '1990', 'link': 'https://www.divan.ru/product/bra-babl-black'}
2024-08-28 12:50:57 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Бабл-3 - 6190
2024-08-28 12:50:57 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-babl-3>
{'name': 'Подвесной светильник Бабл-3', 'price': '6190', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-babl-3'}
2024-08-28 12:50:57 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-sanset-white> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:57 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-babl-9> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:57 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/torsher-billi-black> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:57 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Сансет White - 3690
2024-08-28 12:50:57 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-sanset-white>
{'name': 'Подвесной светильник Сансет White', 'price': '3690', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-sanset-white'}
2024-08-28 12:50:57 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Бабл-9 - 16490
2024-08-28 12:50:57 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-babl-9>
{'name': 'Подвесной светильник Бабл-9', 'price': '16490', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-babl-9'}
2024-08-28 12:50:57 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/torsher-vario-white> (referer: https://www.divan.ru/category/svet) 
2024-08-28 12:50:57 [lighting] DEBUG: Извлеченные данные продукта: Торшер Билли Black - 12990
2024-08-28 12:50:57 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/torsher-billi-black>
{'name': 'Торшер Билли Black', 'price': '12990', 'link': 'https://www.divan.ru/product/torsher-billi-black'}
2024-08-28 12:50:57 [lighting] DEBUG: Извлеченные данные продукта: Торшер Варио White - 3999
2024-08-28 12:50:57 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/torsher-vario-white>
{'name': 'Торшер Варио White', 'price': '3999', 'link': 'https://www.divan.ru/product/torsher-vario-white'}
2024-08-28 12:50:58 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/bra-vario-black> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:58 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/torsher-babl-1> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:58 [lighting] DEBUG: Извлеченные данные продукта: Бра Варио Black - 990
2024-08-28 12:50:58 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/bra-vario-black>
{'name': 'Бра Варио Black', 'price': '990', 'link': 'https://www.divan.ru/product/bra-vario-black'}
2024-08-28 12:50:58 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/torsher-vena-black> (referer: https://www.divan.ru/category/svet)  
2024-08-28 12:50:58 [lighting] DEBUG: Извлеченные данные продукта: Торшер Бабл-1 - 6190
2024-08-28 12:50:58 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/torsher-babl-1>
{'name': 'Торшер Бабл-1', 'price': '6190', 'link': 'https://www.divan.ru/product/torsher-babl-1'}
2024-08-28 12:50:58 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-dendi-black> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:58 [lighting] DEBUG: Извлеченные данные продукта: Торшер Вена Black - 9990
2024-08-28 12:50:58 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/torsher-vena-black>
{'name': 'Торшер Вена Black', 'price': '9990', 'link': 'https://www.divan.ru/product/torsher-vena-black'}
2024-08-28 12:50:58 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Дэнди Black - 2990
2024-08-28 12:50:58 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-dendi-black>
{'name': 'Настольная лампа Дэнди Black', 'price': '2990', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-dendi-black'}
2024-08-28 12:50:58 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-grover-glass> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:58 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Гровер Glass - 3990
2024-08-28 12:50:58 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-grover-glass>
{'name': 'Настольная лампа Гровер Glass', 'price': '3990', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-grover-glass'}
2024-08-28 12:50:58 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-dendi-white> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:58 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Дэнди White - 2990
2024-08-28 12:50:58 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-dendi-white>
{'name': 'Настольная лампа Дэнди White', 'price': '2990', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-dendi-white'}
2024-08-28 12:50:58 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-sfera-orange> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:59 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Сфера Orange - None
2024-08-28 12:50:59 [lighting] ERROR: Отсутствуют название или цена на https://www.divan.ru/product/nastolnaya-lampa-sfera-orange
2024-08-28 12:50:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-kaya-black> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:59 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Кая Black - 2590
2024-08-28 12:50:59 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-kaya-black>
{'name': 'Подвесной светильник Кая Black', 'price': '2590', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-kaya-black'}
2024-08-28 12:50:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/bra-galdakao> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-gross-white> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:59 [lighting] DEBUG: Извлеченные данные продукта: Бра Galdakao-1 - 6590
2024-08-28 12:50:59 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/bra-galdakao>
{'name': 'Бра Galdakao-1', 'price': '6590', 'link': 'https://www.divan.ru/product/bra-galdakao'}
2024-08-28 12:50:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-sensil-silver> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:59 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Гросс White - 3590
2024-08-28 12:50:59 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-gross-white>
{'name': 'Настольная лампа Гросс White', 'price': '3590', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-gross-white'}
2024-08-28 12:50:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-sphere> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:59 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Сэнсил Silver - 4590
2024-08-28 12:50:59 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-sensil-silver>
{'name': 'Подвесной светильник Сэнсил Silver', 'price': '4590', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-sensil-silver'}
2024-08-28 12:50:59 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Sphere - 6530
2024-08-28 12:50:59 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-sphere>
{'name': 'Настольная лампа Sphere', 'price': '6530', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-sphere'}
2024-08-28 12:50:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-layham> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:50:59 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Layham - 19790
2024-08-28 12:50:59 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-layham>
{'name': 'Подвесной светильник Layham', 'price': '19790', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-layham'}
2024-08-28 12:50:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/torsher-duetto> (referer: https://www.divan.ru/category/svet)      
2024-08-28 12:51:00 [lighting] DEBUG: Извлеченные данные продукта: Торшер Duetto - 6990
2024-08-28 12:51:00 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/torsher-duetto>
{'name': 'Торшер Duetto', 'price': '6990', 'link': 'https://www.divan.ru/product/torsher-duetto'}
2024-08-28 12:51:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-sfera-black> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-townshend-4> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:00 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Сфера Black - 3990
2024-08-28 12:51:00 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-sfera-black>
{'name': 'Настольная лампа Сфера Black', 'price': '3990', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-sfera-black'}
2024-08-28 12:51:00 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Townshend-4 - 10990
2024-08-28 12:51:00 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-townshend-4>
{'name': 'Подвесной светильник Townshend-4', 'price': '10990', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-townshend-4'}
2024-08-28 12:51:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/lyustra-monti-3-white> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-tureis> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:00 [lighting] DEBUG: Извлеченные данные продукта: Люстра Монти-3 White - 9990
2024-08-28 12:51:00 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/lyustra-monti-3-white>
{'name': 'Люстра Монти-3 White', 'price': '9990', 'link': 'https://www.divan.ru/product/lyustra-monti-3-white'}
2024-08-28 12:51:00 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Tureis - 3390
2024-08-28 12:51:00 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-tureis>
{'name': 'Подвесной светильник Tureis', 'price': '3390', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-tureis'}
2024-08-28 12:51:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-milligan> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-junior-2> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:00 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Milligan - 5490
2024-08-28 12:51:00 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-milligan>
{'name': 'Подвесной светильник Milligan', 'price': '5490', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-milligan'}
2024-08-28 12:51:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-spajk-orange> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:01 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Junior-2 - 2890
2024-08-28 12:51:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-junior-2>
{'name': 'Настольная лампа Junior-2', 'price': '2890', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-junior-2'}
2024-08-28 12:51:01 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Спайк Orange - 990
2024-08-28 12:51:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-spajk-orange>
{'name': 'Настольная лампа Спайк Orange', 'price': '990', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-spajk-orange'}
2024-08-28 12:51:01 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/spot-lajt-1-black> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:01 [lighting] DEBUG: Извлеченные данные продукта: Спот Лайт-1 Black - 2390
2024-08-28 12:51:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/spot-lajt-1-black>
{'name': 'Спот Лайт-1 Black', 'price': '2390', 'link': 'https://www.divan.ru/product/spot-lajt-1-black'}
2024-08-28 12:51:01 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-junior-1> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:01 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Junior-1 - 3990
2024-08-28 12:51:01 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-junior-1>
{'name': 'Настольная лампа Junior-1', 'price': '3990', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-junior-1'}
2024-08-28 12:51:02 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-junior-4> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:02 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Junior-4 - 2990
2024-08-28 12:51:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-junior-4>
{'name': 'Настольная лампа Junior-4', 'price': '2990', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-junior-4'}
2024-08-28 12:51:02 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-raffi-round> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:02 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/torsher-gross-white> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:02 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Раффи Round - 5990
2024-08-28 12:51:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-raffi-round>
{'name': 'Настольная лампа Раффи Round', 'price': '5990', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-raffi-round'}
2024-08-28 12:51:02 [lighting] DEBUG: Извлеченные данные продукта: Торшер Гросс White - 5990
2024-08-28 12:51:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/torsher-gross-white>
{'name': 'Торшер Гросс White', 'price': '5990', 'link': 'https://www.divan.ru/product/torsher-gross-white'}
2024-08-28 12:51:02 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/bra-moderli-alina> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:02 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/svetilnik-potolochnyj-matthew> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:02 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-mashrum-grey> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:02 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-rej-white> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:02 [lighting] DEBUG: Извлеченные данные продукта: Бра Moderli Alina - 3190
2024-08-28 12:51:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/bra-moderli-alina>
{'name': 'Бра Moderli Alina', 'price': '3190', 'link': 'https://www.divan.ru/product/bra-moderli-alina'}
2024-08-28 12:51:02 [lighting] DEBUG: Извлеченные данные продукта: Светильник потолочный Matthew - 4990
2024-08-28 12:51:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/svetilnik-potolochnyj-matthew>
{'name': 'Светильник потолочный Matthew', 'price': '4990', 'link': 'https://www.divan.ru/product/svetilnik-potolochnyj-matthew'}
2024-08-28 12:51:02 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Машрум Grey - 3990
2024-08-28 12:51:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-mashrum-grey>
{'name': 'Настольная лампа Машрум Grey', 'price': '3990', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-mashrum-grey'}
2024-08-28 12:51:02 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Рэй White - 2590
2024-08-28 12:51:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-rej-white>
{'name': 'Настольная лампа Рэй White', 'price': '2590', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-rej-white'}
2024-08-28 12:51:03 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/torsher-vario-black> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:03 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-maro-green> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:03 [lighting] DEBUG: Извлеченные данные продукта: Торшер Варио Black - 4990
2024-08-28 12:51:03 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/torsher-vario-black>
{'name': 'Торшер Варио Black', 'price': '4990', 'link': 'https://www.divan.ru/product/torsher-vario-black'}
2024-08-28 12:51:03 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Маро Green - 11690
2024-08-28 12:51:03 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-maro-green>
{'name': 'Подвесной светильник Маро Green', 'price': '11690', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-maro-green'}
2024-08-28 12:51:03 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/torsher-rej-white> (referer: https://www.divan.ru/category/svet)   
2024-08-28 12:51:03 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-spajk-green> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:03 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/torsher-mun-black> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:03 [lighting] DEBUG: Извлеченные данные продукта: Торшер Рэй White - 4990
2024-08-28 12:51:03 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/torsher-rej-white>
{'name': 'Торшер Рэй White', 'price': '4990', 'link': 'https://www.divan.ru/product/torsher-rej-white'}
2024-08-28 12:51:03 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Спайк Green - None
2024-08-28 12:51:03 [lighting] ERROR: Отсутствуют название или цена на https://www.divan.ru/product/nastolnaya-lampa-spajk-green
2024-08-28 12:51:03 [lighting] DEBUG: Извлеченные данные продукта: Торшер Мун Black - 5990
2024-08-28 12:51:03 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/torsher-mun-black>
{'name': 'Торшер Мун Black', 'price': '5990', 'link': 'https://www.divan.ru/product/torsher-mun-black'}
2024-08-28 12:51:03 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/nastolnaya-lampa-rej-black> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:03 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-portland-black> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:03 [lighting] DEBUG: Извлеченные данные продукта: Настольная лампа Рэй Black - 2990
2024-08-28 12:51:03 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/nastolnaya-lampa-rej-black>
{'name': 'Настольная лампа Рэй Black', 'price': '2990', 'link': 'https://www.divan.ru/product/nastolnaya-lampa-rej-black'}
2024-08-28 12:51:03 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Портланд Black - 1990
2024-08-28 12:51:03 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-portland-black>
{'name': 'Подвесной светильник Портланд Black', 'price': '1990', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-portland-black'}
2024-08-28 12:51:04 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-kendel-black> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:04 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Кэндел Black - 2690
2024-08-28 12:51:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-kendel-black>
{'name': 'Подвесной светильник Кэндел Black', 'price': '2690', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-kendel-black'}
2024-08-28 12:51:04 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/torsher-vena-beige> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:04 [lighting] DEBUG: Извлеченные данные продукта: Торшер Вена Beige - 9990
2024-08-28 12:51:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/torsher-vena-beige>
{'name': 'Торшер Вена Beige', 'price': '9990', 'link': 'https://www.divan.ru/product/torsher-vena-beige'}
2024-08-28 12:51:05 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.divan.ru/product/podvesnoj-svetilnik-kendel-white> (referer: https://www.divan.ru/category/svet)
2024-08-28 12:51:05 [lighting] DEBUG: Извлеченные данные продукта: Подвесной светильник Кэндел White - 2690
2024-08-28 12:51:05 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.divan.ru/product/podvesnoj-svetilnik-kendel-white>
{'name': 'Подвесной светильник Кэндел White', 'price': '2690', 'link': 'https://www.divan.ru/product/podvesnoj-svetilnik-kendel-white'}
2024-08-28 12:51:05 [scrapy.core.engine] INFO: Closing spider (finished)
2024-08-28 12:51:05 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 19135,
 'downloader/request_count': 50,
 'downloader/request_method_count/GET': 50,
 'downloader/response_bytes': 2696696,
 'downloader/response_count': 50,
 'downloader/response_status_count/200': 50,
 'dupefilter/filtered': 144,
 'elapsed_time_seconds': 13.237484,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2024, 8, 28, 8, 51, 5, 176078, tzinfo=datetime.timezone.utc),
 'httpcompression/response_bytes': 15246273,
 'httpcompression/response_count': 50,
 'item_scraped_count': 46,
 'log_count/DEBUG': 150,
 'log_count/ERROR': 2,
 'log_count/INFO': 13,
 'request_depth_max': 1,
 'response_received_count': 50,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 49,
 'scheduler/dequeued/memory': 49,
 'scheduler/enqueued': 49,
 'scheduler/enqueued/memory': 49,
 'start_time': datetime.datetime(2024, 8, 28, 8, 50, 51, 938594, tzinfo=datetime.timezone.utc)}
2024-08-28 12:51:05 [scrapy.core.engine] INFO: Spider closed (finished)
PS C:\_Python AI\github\PS05-web-scraping\divanpars> 
