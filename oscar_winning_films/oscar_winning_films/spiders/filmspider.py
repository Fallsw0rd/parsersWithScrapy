import scrapy


# Паук filmspider
class FilmspiderSpider(scrapy.Spider):
    name = "filmspider"
    allowed_domains = ["scrapethissite.com"]
    start_urls = ["https://scrapethissite.com/pages/ajax-javascript/"]

    def parse(self, response, **kwargs):
        # Парсинг годов для формирования ссылок на фильмы
        years = response.xpath("//section/div/div[4]/div/a/text()").getall()

        for year in years:
            # Формирование URL-адреса по годам
            year_link = f"{self.start_urls[0]}/?ajax=true&year={year}"
            # Запрос к веб-сайту для получения фильмов по годам
            yield scrapy.Request(response.urljoin(year_link), self.parse_films)

    # Функция parse_films для парсинга фильмов и экспорта JSON-файла
    def parse_films(self, response):
        for film in response.json():
            yield {
                "Title": film["title"].strip(),
                "Nominations": str(film["nominations"]),
                "Awards": str(film["awards"]),
                # Если у строки в таблице "Лучший фильм" не найден, записываем False
                "Best Picture": str(film.get("best_picture", False))
            }
