from django.core.management.base import BaseCommand
from articles.scheduler import RSS_FEEDS
from articles.rss_parser import fetch_articles

class Command(BaseCommand):
    help = "Fetch articles from all RSS feeds"

    def handle(self, *args, **kwargs):
        fetch_articles(RSS_FEEDS)  # Pass the same feed list
        self.stdout.write(self.style.SUCCESS("Successfully fetched articles. ✅"))
