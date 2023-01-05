import include


def create_server_connection():
    try:
        mydb = include.sql.connect('data.db')
        print("Connection Successful")
    except include.sql.Error as err:
        print(f"Error: '{err}")
    return mydb


connection = create_server_connection()


def insert_data(connection, data):
    cursor = connection.cursor()
    url = data[0]
    source = data[1]
    final = zip(url, source)
    for x in final:
        cursor.execute(
            "INSERT INTO news (site, source) VALUES (? , ?)", x)
    connection.commit()
