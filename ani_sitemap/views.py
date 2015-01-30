from django.contrib.sitemaps import Sitemap
from aninews.models import NewsItem
from django.utils import timezone
# Create your views here.

class NewsSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return NewsItem.objects.filter(published < timezone.now())

    def lastmod(self, obj):
        return obj.published

