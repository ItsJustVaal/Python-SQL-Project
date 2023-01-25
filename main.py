import include

connection = include.help.create_server_connection()

include.db.insert_data(connection)
