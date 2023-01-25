import include

DATE = include.dt.now().strftime("%Y-%m-%d %H:%M:%S")


def insert_data(connection):
    # This needs to be rewritten to work lol
    zipper = include.sc.scrape()
    with open("JSONs/links.JSON") as f:
        current_links = include.json.load(f).split('", "')

    final_links = []
    for x in current_links:
        final_links.append(x.replace(u"\\u2018", "'").replace(
            u"\\u2019", "'").replace(u"\\u00a3", '£').replace(
            u"\\u2013", '-').replace(u"\\u201d", "'").replace(u"\\u201c", "'"))

    with open("JSONs/sources.JSON") as f:
        current_sources = include.json.load(f)

    cursor = connection.cursor()
    try:
        cursor.execute(
            "CREATE TABLE news (id INTEGER PRIMARY KEY AUTOINCREMENT, site TEXT NOT NULL, source_id INT NOT NULL, datetime TEXT NOT NULL);")
        print("Table Created: news")
    except include.sql.Error as err:
        print(err)
    try:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS sources (id INT NOT NULL, source TEXT NOT NULL, FOREIGN KEY(id) REFERENCES news (source_id));")
        print("Table Created: sources")
    except include.sql.Error as err:
        print(err)

    for item in zipper:
        if item[1] in current_sources.keys():
            final_string = (item[0], current_sources[item[1]], DATE)
            cursor.execute("SELECT site FROM news WHERE site = ?", (item[0],))
            check = cursor.fetchall()
            if len(check) == 0:
                try:
                    cursor.execute(
                        "INSERT INTO news (site, source_id, datetime) VALUES (?, ?, ?)", final_string)
                    print(f'Inserted: {item[0]}')
                except include.sql.Error as err:
                    print(err)
            else:
                print('Headline already in DB')

    for item in current_sources:
        final_string = (current_sources[item], item)
        cursor.execute("SELECT source FROM sources WHERE source = ?", (item,))
        check = cursor.fetchall()
        if len(check) == 0:
            try:
                cursor.execute(
                    "INSERT INTO sources (id, source) VALUES (?, ?)", final_string)
                print(f'Inserted: {item}')
            except include.sql.Error as err:
                print(err)
        else:
            print('Source already in DB')

    connection.commit()

# include.help.get_all()
