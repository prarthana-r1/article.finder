from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils.timezone import now
from .rss_parser import fetch_articles

# List of RSS feeds (single source of truth)
RSS_FEEDS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "https://feeds.bbci.co.uk/news/technology/rss.xml",
    "https://www.theguardian.com/uk/technology/rss",
    "https://www.cnet.com/rss/news/",
    "https://www.wired.com/feed/rss",
    "https://techcrunch.com/feed/",
    "https://mashable.com/feeds/rss/tech",
    "https://www.engadget.com/rss.xml",
    "https://www.zdnet.com/news/rss.xml",
]

def start_scheduler(sender, **kwargs):
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
        fetch_articles,
        "interval",
        minutes=1,
        args=[RSS_FEEDS],  # Pass the full list of feeds
        next_run_time=now()  # Start immediately
    )

    print("Starting scheduler... 🚀")
    scheduler.start()
