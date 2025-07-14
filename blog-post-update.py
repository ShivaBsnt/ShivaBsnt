import feedparser

BLOG_RSS_FEED = "https://www.shivabahadurbasnet.com.np/feed.xml"
MAX_POSTS = 5
README_FILE = "README.md"

import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

def fetch_latest_posts():
    feed = feedparser.parse(BLOG_RSS_FEED, )
    latest_posts = []
    for entry in feed.entries[:MAX_POSTS]:
        title = entry.title
        link = entry.link
        latest_posts.append(f"- [{title}]({link})")
    print(latest_posts)
    return latest_posts

def update_readme(posts):
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    marker_start = "<!-- BLOG-POST-LIST:START -->"
    marker_end = "<!-- BLOG-POST-LIST:END -->"
    start = content.find(marker_start) + len(marker_start)
    end = content.find(marker_end)

    new_content = content[:start] + "\n" + "\n".join(posts) + "\n" + content[end:]

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    posts = fetch_latest_posts()
    update_readme(posts)
