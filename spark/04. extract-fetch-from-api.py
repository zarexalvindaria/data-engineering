import requests

# Fetch the Hackernews post
resp = requests.____("https://hacker-news.firebaseio.com/v0/item/16222426.json")

# Print the response parsed as JSON
print(resp.____())

# Assign the score of the test to post_score
post_score = resp.___()["____"]
print(post_score)

----

import requests

# Fetch the Hackernews post
resp = requests.get("https://hacker-news.firebaseio.com/v0/item/16222426.json")

# Print the response parsed as JSON
print(resp.json())

# Assign the score of the test to post_score
post_score = resp.json()["score"]
print(post_score)
{'by': 'neis', 'descendants': 0, 'id': 16222426, 'score': 17, 'time': 1516800333, 'title': 'Duolingo-Style Learning for Data Science: DataCamp for Mobile', 'type': 'story', 'url': 'https://medium.com/datacamp/duolingo-style-learning-for-data-science-datacamp-for-mobile-3861d1bc02df'}
17