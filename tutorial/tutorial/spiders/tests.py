inList = response.xpath('//ol').extract()

class Celular(scrapy.item):
    Imagem = scrapy.Field()
    Nome = scrapy.Field()
    Price = scrapy.Field()
    Desconto = scrapy.Field()
    Vendedor = scrapy.Field()
    InfoAdicional = scrapy.Field()
    
for celular in inList:
    item = Celular()
    item['Imagem'] = celular.xpath('.//div[contains(@class, "image-content")]/a/@href').extract()
    item['Nome'] = celular.xpath('//ol//div/h2/a/span/text()').extract()
    item['Price'] = celular.xpath('//ol//div/div/span[@class="price__fraction"]/text()').extract()
    item['Desconto'] =celular.xpath('.//div[contains(@class, "item__discount")]/text()').extract()
    item['Vendedor'] = celular.xpath('//div[contains(@class,"item__brand")]//span/text()').extract()
    item['NumeroDeReviews'] = celular.xpath('//div[contains(@class,"item__reviews-total")]/text()').extract()
    item['InfoAdicional'] = celular.xpath('.//p[contains(@class, "stack-item-info")]/text()').extract()
        
