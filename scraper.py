# everything imports include because include imports everything
import include

'''
Scrapes the site https://www.footballnews.net/ legally
legally to obtain football news headlines
'''
URL = 'https://www.footballnews.net/'


def scrape():

    # Get request and html parser
    try:
        page = include.rq.get(URL)
    except:
        print("error")
    data = include.bs(page.content, "html.parser")

    # Setting variables based on the html
    results = data.find(id='content')
    news = results.find("div", class_='content-data')
    final = news.find("ul", class_="news-content")
    html_links = final.find_all("a")
    html_sources = final.find_all("span", class_="source")

    # Decided to make this relational instead of combining them
    links = [link.text.strip() for link in html_links]
    sources = [source.text.strip().replace("-", '').replace(' ', '').lower()
               for source in html_sources]
    zipped_file = zip(links, sources)
    sources_dict = dict()
    for num in range(len(set(sources))):
        if sources[num] not in sources_dict:
            sources_dict[sources[num]] = num

    if links and sources:
        print("Success, saving")
    else:
        print("Failed")
        return
    file_data = include.json.dumps(links)
    with open('jsons/links.json', 'w') as file:
        include.json.dump(file_data, file)

    with open('jsons/sources.json', 'w') as file:
        include.json.dump(sources_dict, file)

    print("complete")
    return zipped_file
