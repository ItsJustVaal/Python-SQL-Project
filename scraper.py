import include
'''
Scrapes the site https://www.footballnews.net/ legally
legally to obtain football news headlines
'''
URL = 'https://www.footballnews.net/'


def scrape():

    # open blacklist
    with open('C:\Temp\Code\Learn\Practice\Scraper\\blacklist.txt', 'r') as f:
        data = f.readlines()
    blacklist = [item.strip('\n') for item in data]
    if not blacklist:
        print("Failed to pull blacklist")

    # Get request
    try:
        page = include.rq.get(URL)
    except:
        print("error")

    # Setting variables and getting data based on the html
    print("Parsing HTML")
    data = include.bs(page.content, "html.parser")
    results = data.find(id='content')
    news = results.find("div", class_='content-data')
    final = news.find("ul", class_="news-content")
    html_links = final.find_all("a")
    html_sources = final.find_all("span", class_="source")

    '''
    Goes through each tuple in the list and checks the source
    If the source is in the black list it deletes it
    otherwise it creates a list that zips the headline
    and source together and sends it to the insert function
    '''
    links = [link.text.strip().lower() for link in html_links]
    sources = list(set([source.text.strip().replace("-", '').replace(' ', '').lower()
                   for source in html_sources]))
    # checks if something exists
    if links and sources:
        print("Successfully scraped site, Filtering Data")
    else:
        print("Failed to scrape")
        return

    # Filters the list and source dict based on the blacklist
    print("Filtering for blacklist")
    zipped_file = list(zip(links, sources))
    print("Original Data entered")
    final = [(val, key) for (val, key) in zipped_file if key not in blacklist]
    print("Filtering Data complete")

    # Filters sources and creates the dictionary
    print("Creating Sources Dictionary")
    sources_dict = dict()
    for num in range(len(sources)):
        if sources[num] not in sources_dict and sources[num] not in blacklist:
            sources_dict[sources[num]] = num
        else:
            continue

    # Creates JSON of sources
    print("Saving JSON back up of sources mapping")
    with open('jsons/sources.json', 'w') as file:
        include.json.dump(sources_dict, file)

    print("Complete")
    return final
