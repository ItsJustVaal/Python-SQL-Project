import include

DATE = include.dt.now().strftime("%Y-%m-%d %H:%M:%S")

def insert_data(connection):
    
    # Get zipped list of tuples from scrape
    zipper = include.sc.scrape()

    # Get dictionary of sources and their id key
    with open("JSONs/sources.JSON") as f:
        current_sources = include.json.load(f)

    # Create cursor and initiates tables if they dont exist
    cursor = connection.cursor()
    try:
        cursor.execute(
            "CREATE TABLE news (id INTEGER PRIMARY KEY AUTOINCREMENT, site TEXT NOT NULL, source_id INT NOT NULL, datetime TEXT NOT NULL);")
        print("Table Created: news")
    except include.sql.Error as err:
        print(err)
    try:
        cursor.execute(
            "CREATE TABLE sources (id INT NOT NULL, source TEXT NOT NULL, FOREIGN KEY(id) REFERENCES news (source_id));")
        print("Table Created: sources")
    except include.sql.Error as err:
        print(err)

    new_sources = 0
    for item in current_sources:
        final_string = (current_sources[item], item)
        cursor.execute("SELECT source FROM sources WHERE source = ? OR id = ?;",
                       (item, current_sources[item]))
        check = cursor.fetchall()
        if len(check) == 0:
            new_sources = new_sources + 1
            try:
                cursor.execute(
                    "INSERT INTO sources (id, source) VALUES (?, ?);", final_string)
            except include.sql.Error as err:
                print(err)


    cursor.execute("SELECT source, id FROM sources;")
    get_all_sources = dict(cursor.fetchall())
    
    new_headlines = 0
    for item in zipper:
        if item[1] in get_all_sources.keys():
            final_string = (item[0], get_all_sources[item[1]], DATE)
            cursor.execute("SELECT site FROM news WHERE site = ?;", (item[0],))
            check = cursor.fetchall()
            if len(check) == 0:
                new_headlines = new_headlines + 1
                try:
                    cursor.execute(
                        "INSERT INTO news (site, source_id, datetime) VALUES (?, ?, ?);", final_string)
                except include.sql.Error as err:
                    print(err)
    connection.commit()

    print(f"{new_sources} sources added")
    print(f"{new_headlines} headlines added")
    print("Complete")
