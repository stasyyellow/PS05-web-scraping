import scrapy

class LightingSpider(scrapy.Spider):
    name = 'lighting'
    allowed_domains = ['divan.ru']
    start_urls = ['https://www.divan.ru/category/svet']

    def parse(self, response):
        self.logger.info(f'Обработка URL: {response.url}')

        # Извлечение всех ссылок на продукты освещения
        product_urls = response.css('a[href*="/product/"]::attr(href)').extract()
        self.logger.info(f'Количество найденных URL продуктов: {len(product_urls)}')

        if product_urls:
            for product_url in product_urls:
                yield response.follow(product_url, callback=self.parse_product)
        else:
            self.logger.warning('URL продуктов не обнаружены!')

        # Переход на следующую страницу, если она есть
        next_page_url = response.css('a.pagination__next::attr(href)').get()
        if next_page_url:
            self.logger.info(f'Переход на следующую страницу: {next_page_url}')
            yield response.follow(next_page_url, callback=self.parse)
        else:
            self.logger.info('Следующая страница не найдена.')

    def parse_product(self, response):
        # Получение информации о продукте
        product_name = response.css('h1[itemprop="name"]::text').get()
        product_price = response.css('span[itemprop="price"]::attr(content)').get()
        self.logger.debug(f'Извлеченные данные продукта: {product_name} - {product_price}')

        if product_name and product_price:
            yield {
                'name': product_name,    #<span itemprop="name">Подвесной светильник Сансет Black</span>
                'price': product_price,  #<span class="ui-LD-ZU ui-SVNym bSEDs" data-testid="price">5990<span class="ui-i5wwi ui-VDyJR ui-VWOa-">руб.</span></span>
                'link': response.url     #<a tabindex="0" class="ui-GPFV8 qUioe ProductName ActiveProduct cursor-on-hover" href="/product/podvesnoj-svetilnik-sanset-black"><span itemprop="name" class="cursor-on-hover">Подвесной светильник Сансет Black</span></a>
            }
        else:
            self.logger.error(f'Отсутствуют название или цена на {response.url}')

