import scrapy

print("=====SEJA BEM VINDO AO CRAWLER PARA O MERCADO LIVRE")
linkCrawl = input("=====DIGITE O ITEM QUE DESEJA BUSCAR: ")
print("So um momento, estamos procurando por " + linkCrawl + "...")





class MLSpider(scrapy.Spider):
    name = "mlspider"

    def start_requests(self):
        urls = ["https://celulares.mercadolivre.com.br/celular",
                "https://lista.mercadolivre.com.br/geladeiras#D[A:geladeiras]"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'mlcel-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = scrapy.Item()
        item['Imagem'] = response.xpath('.//div[contains(@class, "image-content")]/a/@href').extract()
        item['Nome'] = response.xpath('//ol//div/h2/a/span/text()').extract()
        item['Price'] = response.xpath('//ol//div/div/span[@class="price__fraction"]/text()').extract()
        item['Desconto'] = response.xpath('.//div[contains(@class, "item__discount")]/text()').extract()
        item['Vendedor'] = response.xpath('//div[contains(@class,"item__brand")]//span/text()').extract()
        item['ItensVendidos'] = response.xpath('.//div[contains(@class,"item__condition")]/text()').extract()
        item['InfoAdicional'] = response.xpath('.//p[contains(@class, "stack-item-info")]/text()').extract()
        return item
