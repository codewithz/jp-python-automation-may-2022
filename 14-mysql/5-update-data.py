from mysql.connector import connect, Error

try:
    with connect(
        host='localhost',
        user='root',
        password='admin',
        database='jp_python_batch'
    ) as connection:
        print(connection)
        update_table_query = """
        Update movies set title="%s" ,release_year="%s", genre="%s" where 
        id="%s" 
        
        """ % ('Some TItle', 2020, 'Horror', 1)
        with connection.cursor() as cursor:
            cursor.execute(update_table_query)
            connection.commit()
            print("Data Updated")
except Error as ex:
    print(ex)
