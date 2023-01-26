import include

connection = include.help.create_server_connection()

include.db.insert_data(connection)


# This file is the last thing to flesh out completely since it just runs the program
