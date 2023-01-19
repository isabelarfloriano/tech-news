import requests
import time
import parsel


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"},
        )
        if response.status_code == 200:
            response = response.text
            return response
    except requests.ReadTimeout:
        return None
    else:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = parsel.Selector(html_content)
    links_news = selector.css("a.cs-overlay-link::attr(href)").getall()
    return links_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    link_next_page = selector.css(".next.page-numbers::attr(href)").get()
    return link_next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
