from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_list = []
    news_founded = search_news({"title": {"$regex": title, "$options": "i"}})
    for news in news_founded:
        news_list.append((news["title"], news["url"]))

    return news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
