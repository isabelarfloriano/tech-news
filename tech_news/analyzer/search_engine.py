from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_list = []
    news_founded = search_news({"title": {"$regex": title, "$options": "i"}})
    for news in news_founded:
        news_list.append((news["title"], news["url"]))

    return news_list


# Requisito 7
def search_by_date(date):
    news_list = []
    try:
        date_ISO = datetime.fromisoformat(date)
        date_format = date_ISO.strftime("%d/%m/%Y")
        news_founded = search_news({"timestamp": {"$eq": date_format}})
        for news in news_founded:
            news_list.append((news["title"], news["url"]))

        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news_list = []
    news_founded = search_news({"tags": {"$regex": tag, "$options": "i"}})
    for news in news_founded:
        news_list.append((news["title"], news["url"]))

    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
