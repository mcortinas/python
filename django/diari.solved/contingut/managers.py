# Function get_root_categories for Category manager

from django.db import models
import datetime
from django.utils.timezone import utc

class ArticleManager(models.Manager):
    def get_most_visited(self):
        return self.all().order_by("-num_visits")

    def get_trending_topics(self):
        return self.annotate(num_comments = models.Count("comments")).order_by("-num_comments")

    def get_by_category(self, category):
        return self.filter(category = category)

    def get_published(self):
        now = datetime.datetime.utcnow().replace(tzinfo = utc)
        return self.filter(publish_date__lte = now)

class CategoryManager(models.Manager):
    def get_parents(self):
        return self.filter(parent__isnull = True)

class CommentManager(models.Manager):
    def get_comments_by_article(self, article):
        return self.filter(article = article).order_by("-timestamp")
