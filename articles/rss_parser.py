from dateutil import parser
import requests
from bs4 import BeautifulSoup
from .models import Article

# Add a User-Agent header to mimic a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0"
}

def fetch_articles(feed_urls):
    """
    Fetch articles from multiple RSS feeds and save new ones to the database.
    """
    for feed_url in feed_urls:
        print(f"Fetching articles from: {feed_url}")

        
        try:
            response = requests.get(feed_url, headers=HEADERS, timeout=10)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {feed_url}: {e}")
            continue

        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')

        new_articles = []
        existing_links = set(Article.objects.values_list('link', flat=True))

        for item in items:
            title = item.title.text.strip() if item.title else "No title"
            
            # Try fetching link from <link> tag, fallback to <guid>
            link = None
            if item.link:
                link = item.link.text.strip()
            elif item.find('guid'):
                link = item.find('guid').text.strip()
            
            print(f"Fetched link: {link}")
                
            if not link:
                print(f"Skipping article with missing link: {title}")
                continue

            description = item.description.text.strip() if item.description else "No description"

            try:
                pub_date = parser.parse(item.pubDate.text.strip()) if item.pubDate else None
            except (ValueError, AttributeError):
                pub_date = None

            if link not in existing_links:
                new_articles.append(Article(
                    title=title,
                    link=link,
                    description=description,
                    pub_date=pub_date
                ))

        if new_articles:
            Article.objects.bulk_create(new_articles)
            print(f"Added {len(new_articles)} new articles from {feed_url}")
        else:
            print(f"No new articles from {feed_url}")

    print(f"Total articles in DB: {Article.objects.count()}")
