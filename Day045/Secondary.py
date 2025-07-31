from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# Article titles and links
articles = soup.select(".titleline a")

article_titles = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]

# Article upvotes
article_upvotes = [
    int(score.getText().split()[0])
    for score in soup.select(".score")
]

# Prevent index out of range by checking matching lengths
min_length = min(len(article_titles), len(article_upvotes))

if min_length > 0:
    # Find the article with the most votes
    max_vote_count = max(article_upvotes[:min_length])
    max_vote_count_index = article_upvotes.index(max_vote_count)

    print("Top Article:")
    print(article_titles[max_vote_count_index])
    print(article_links[max_vote_count_index])
else:
    print("No articles or upvotes found.")
