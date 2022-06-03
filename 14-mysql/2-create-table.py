from mysql.connector import connect, Error

try:
    with connect(
        host='localhost',
        user='root',
        password='admin',
        database='jp_python_batch'
    ) as connection:
        print(connection)
        create_table_query = """
        CREATE TABLE movies(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        release_year YEAR(4),
        genre VARCHAR(100),
        collection_in_mil INT)
        """
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit()
            print("Table Created")
except Error as ex:
    print(ex)
