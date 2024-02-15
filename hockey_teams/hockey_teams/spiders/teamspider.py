import scrapy


# Паук teamspider
class TeamspiderSpider(scrapy.Spider):
    name = "teamspider"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/forms/"]

    def parse(self, response, **kwargs):
        # Найдем форму на странице и заполним ее данными
        form_data = {
            "q": 'New York',  # Устанавливаем значение для поискового запроса
            "per_page": "100"  # Устанавливаем значение для пагинации количества хоккейных команд на странице
        }

        # Отправляем форму запроса и указываем метод обратного вызова для обработки ответа
        yield scrapy.FormRequest(url=self.start_urls[0], formdata=form_data, method="GET",
                                 callback=self.parse_after_form)

    def parse_after_form(self, response):
        # Находим таблицу
        table = response.xpath('//table')[0]
        # Получаем заголовки столбцов
        headers = [header.strip() for header in table.xpath('.//th/text()').getall()]
        # Находим строки таблицы
        rows = table.xpath('.//tr[position() > 1]')  # Исключаем первую строку с заголовками

        for row in rows:
            # Получаем значения ячеек строки
            cells = row.xpath('.//td')
            # Создаем словарь для текущей строки
            row_data = {}

            # Заполняем словарь значениями из ячеек строки, соответствующими заголовкам столбцов
            for header, cell in zip(headers, cells):
                value = cell.xpath('string()').get().strip()
                row_data[header] = value

            yield row_data
