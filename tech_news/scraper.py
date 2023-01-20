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
    comments_count = 0

    selector = parsel.Selector(html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments = selector.css(".comment-list li").getall()
    # print(comments)
    for li in comments:
        comments_count = 1
    # print(comments_count)
    summary_list = selector.css(
        ".entry-content > p:first-of-type *::text"
    ).getall()
    summary = "".join(summary_list).strip()
    # print("SUMMARY  " + summary)
    tags = selector.css("section.post-tags a::text").getall()
    category = selector.css("div.meta-category span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
