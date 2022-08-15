from django.db import models


class NewsArticle(models.Model):
    title = models.CharField(max_length=78)
    author = models.CharField(max_length=60)
    description = models.CharField(max_length=288)
    url = models.CharField(max_length=500, null=True)
    urlToImage = models.CharField(max_length=500, null=True)
    publishedAt = models.DateField()
    added = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-publishedAt",)

    def __str__(self) -> str:
        return self.title

class SubscribersEmail(models.Model):
    email = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    sent = models.IntegerField()

    def __str__(self) -> str:
        return self.email
