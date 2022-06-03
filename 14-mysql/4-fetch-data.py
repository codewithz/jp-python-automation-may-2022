from mysql.connector import connect, Error

try:
    with connect(
        host='localhost',
        user='root',
        password='admin',
        database='jp_python_batch'
    ) as connection:
        print(connection)
        select_query = """
        Select title,collection_in_mil
        FROM movies
        """
        with connection.cursor() as cursor:
            cursor.execute(select_query)

            for movie in cursor.fetchall():
                print(movie)
except Error as ex:
    print(ex)
