# Requisito 10
from collections import Counter
from tech_news.database import find_news


def top_5_news():
    top_five_news = []
    news_list = find_news()
    news = sorted(news_list, key=lambda news_list: news_list["title"])
    news_by_comments = sorted(news, key=lambda news: news["comments_count"])
    news_by_comments.reverse()
    top_news = news_by_comments[:5]
    for news in top_news:
        top_five_news.append((news["title"], news["url"]))
    return top_five_news


# Requisito 11
def top_5_categories():
    top_five_categories = []
    news_list = find_news()
    categories = [news["category"] for news in news_list]
    categories.sort()
    categories_counted = Counter(categories)
    for category in categories_counted.most_common():
        top_five_categories.append(category[0])
    return top_five_categories[:5]
