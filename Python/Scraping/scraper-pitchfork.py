import requests
from bs4 import BeautifulSoup

db = []

for i in range(1, 30):

    main_url = "https://pitchfork.com/reviews/albums/?page=" + str(i)
    main_url_rqst = requests.get(main_url)
    soup = BeautifulSoup(main_url_rqst.content, 'html.parser')

    review_links = soup.find_all('a', class_="review__link")

    for i in review_links:
        single_review = {}

        single_link = 'https://pitchfork.com' + i.get('href')
        single_link_scrape = BeautifulSoup(requests.get(single_link).content, 'html.parser')

        single_review["artist"] = single_link_scrape.find('ul', class_='artist-links').get_text()
        single_review["album"] = single_link_scrape.find('h1', class_='single-album-tombstone__review-title').get_text()
        single_review["score"] = single_link_scrape.find('span', class_='score').get_text()

        db.append(single_review)

print(db)



