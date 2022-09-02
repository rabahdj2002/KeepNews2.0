import time
from datetime import datetime
from distutils import core

import requests
from core.settings import ALLOWED_HOSTS
from frontend.models import NewsArticle


def getNews(topics=['ukraine', 'russia', 'war', 'putin', 'zelensky'], limit="50"):
    for topic in topics:
        url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/NewsSearchAPI"
        querystring = {"q": topic, "pageNumber": "1", "pageSize": limit, "autoCorrect": "true",
                       "withThumbnails": "true", "fromPublishedDate": "null", "toPublishedDate": "null"}
        headers = {
            "X-RapidAPI-Key": "22606cdc51mshb55e1156ae0b717p1f67c2jsn0b17cef6e7c0",
            "X-RapidAPI-Host": "contextualwebsearch-websearch-v1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        articles = response.json()
        total = 0
        for article in articles['value']:
            if article['image']["url"]:
                title = article['title']
                description = article['description']
                url = article["url"].replace(" ", "")
                urlToImage = article["image"]['url'].replace(" ", "")
                publishedAt = datetime.fromisoformat(article['datePublished'].split(
                    'T')[0] + "+" + article['datePublished'].split('T')[-1].replace(" ", ""))
                author = article['provider']['name']
                if title is not None and len(title) > 90:
                    title = title[:86]+" ..."
                if description is not None and description.strip() != "" and len(description) > 250:
                    description = description[:246]+" ..."
                if not NewsArticle.objects.filter(url=url) and not NewsArticle.objects.filter(title=title):
                    new_article = NewsArticle(title=title, author=author, description=description, url=url,
                                              urlToImage=urlToImage, publishedAt=publishedAt)
                    new_article.save()
                    total += 1
        print(f"Fetched {total} Articles For {topic}.")
        time.sleep(1)


def keepAlive():
    x = requests.get(ALLOWED_HOSTS[0])
    print(x.status_code)
