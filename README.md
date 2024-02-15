# Парсинг с помощью Scrapy

Парсинг двух страниц сайта [Scrape This Site](https://www.scrapethissite.com/), а именно страница [с фильмами по годам](https://www.scrapethissite.com/pages/ajax-javascript/) и страница [с хоккейными командами](https://www.scrapethissite.com/pages/forms/).

## Установка

1. Клонировать репозиторий:

    ```bash
    git clone https://github.com/Fallsw0rd/parsersWithScrapy.git
    ```

2. Перейти в директорию проекта:

    ```bash
    cd parsersWithScrapy
    ```
    
3. Cоздание виртуального окружения:
    
    ```bash
    python -m venv venv
    ```

4. Активация виртуального окружения:
    
   Для Windows:

    ```bash
    venv\Scripts\activate.bat
    ```

    Для Linux и MacOS:
    
    ```bash
    source venv/bin/activate
    ```

5. Установка зависимостей:

    ```bash
    pip install -r requirements.txt
    ```

## Использование

### Для парсинга с фильмами по годам:

1. Перейти в проект oscar_winning_films:
    ```bash 
    cd oscar_winning_films
    ```
    
2. Запустить паука для парсинга:
    ```bash
    scrapy crawl filmspider
    ```
    
После парсинга в проекте создается JSON-файл с результатом парсинга.

***

### Для парсинга с хоккейными командами с формой:

1. Перейти в проект hockey_teams:
    ```bash 
    cd hockey_teams
    ```
    
2. Запустить паука для парсинга:
    ```bash
    scrapy crawl teamspider
    ```
    
После парсинга в проекте создается JSON-файл с результатом парсинга.

***

### Мои контакты
#### [Мой Github](https://github.com/Fallsw0rd)
#### [Мой Discord!](https://discordapp.com/users/573143926442295306/ )