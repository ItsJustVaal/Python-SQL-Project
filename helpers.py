import include
# this file is just a couple functions to clear the tables so I dont have to keep typing everything out becacuse im lazy

def create_server_connection():
    try:
        mydb = include.sql.connect('data.db')
        print("Connection Successful")
    except include.sql.Error as err:
        print(f"Error: '{err}")
    return mydb


def clear_table():
    connect = create_server_connection()
    mouse = connect.cursor()
    mouse.execute("DELETE FROM news;")
    sel = mouse.execute("SELECT * FROM news;")
    connect.commit()
    if sel:
        print("Table Clear")
    else:
        print("Try Again: ", sel.fetchall())


def get_all():
    connect = create_server_connection()
    mouse = connect.cursor()
    sel = mouse.execute("SELECT * FROM news;")
    print(sel.fetchall())
