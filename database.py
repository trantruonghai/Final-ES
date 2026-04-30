imoport (mysql) #ten database
def get_db():
    return (mysql).connect(
        host="localhost",
        user="root",
        password="",
        database="librarydb",
    )
