# everything imports include because include imports everything
import include

'''
Scrapes the site https://www.footballnews.net/ legally
legally to obtain football news headlines
'''


def scrape(sql=False):

    # Get request and html parser
    URL = 'https://www.footballnews.net/'
    page = include.rq.get(URL)
    data = include.bs(page.content, "html.parser")

    # Setting variables based on the html
    results = data.find(id='content')
    news = results.find("div", class_='content-data')
    final = news.find("ul", class_="news-content")
    html_links = final.find_all("a")
    html_sources = final.find_all("span", class_="source")

    # Makes two lists with the URLs and their source
    links, sources = [], []
    for link in html_links:
        links.append(link.text.strip())
    for source in html_sources:
        k = source.text.strip().replace("-", '')
        sources.append(' '.join(k.split()))

    # Combines the two lists and makes a
    # hashmap with the combined lists
    combined = zip(links, sources)
    url_final = {}
    for i, x in enumerate(combined):
        url_final[i] = x

    # If this is for my database I will call scrape()
    # with True as the argument which will convert and
    # it will return the two lists for proper SQL entry
    # otherwise it will dump the hashmap in json fileform
    if sql == True:
        return links, sources

    file_data = include.json.dumps(url_final)
    with open('jsons/data.json', 'w') as file:
        include.json.dump(file_data, file)


scrape(True)
