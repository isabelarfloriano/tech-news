import sys
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.search_engine import search_by_tag
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.ratings import top_5_news
from tech_news.scraper import get_tech_news


def call_get_tech_news():
    try:
        amount = int(input("Digite quantas notícias serão buscadas: "))
        get_tech_news(amount)
    except ValueError:
        print("Entrada inválida.")


def call_search_by_title():
    try:
        title = input("Digite o título: ")
        result = search_by_title(title)
        for r in result:
            print(r)
    except Exception as e:
        print(f"Erro: {e}")


def call_search_by_date():
    try:
        data = input("Digite a data no formato aaaa-mm-dd: ")
        result = search_by_date(data)
        for r in result:
            print(r)
    except Exception as e:
        print(f"Erro: {e}")


def call_search_by_tag():
    try:
        tag = input("Digite a tag: ")
        result = search_by_tag(tag)
        for r in result:
            print(r)
    except Exception as e:
        print(f"Erro: {e}")


def call_search_by_category():
    try:
        category = input("Digite a categoria: ")
        result = search_by_category(category)
        for r in result:
            print(r)
    except Exception as e:
        print(f"Erro: {e}")


def call_top_5_news():
    try:
        result = top_5_news()
        for r in result:
            print(r)
    except Exception as e:
        print(f"Erro: {e}")


def call_top_5_categories():
    try:
        result = top_5_categories()
        for r in result:
            print(r)
    except Exception as e:
        print(f"Erro: {e}")


# Requisito 12
def analyzer_menu():
    options = {
        "0": ("Popular o banco com notícias", call_get_tech_news),
        "1": ("Buscar notícias por título", call_search_by_title),
        "2": ("Buscar notícias por data", call_search_by_date),
        "3": ("Buscar notícias por tag", call_search_by_tag),
        "4": ("Buscar notícias por categoria", call_search_by_category),
        "5": ("Listar top 5 notícias", call_top_5_news),
        "6": ("Listar top 5 categorias", call_top_5_categories),
        "7": ("Sair", lambda: print("Encerrando script")),
    }

    while True:
        print("Selecione uma das opções a seguir:")
        for choice, description in options.items():
            print(f" {choice} - {description[0]}")
        choice = input()

        if choice not in options:
            print("Opção inválida", file=sys.stderr)
            continue

        if choice == "7":
            options[choice][1]()
            break

        options[choice][1]()


if __name__ == "__main__":
    analyzer_menu()
