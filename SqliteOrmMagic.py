"""
The script allows you to access the SQlite3 database 
through a function, which is more convenient than 
the syntax of direct SQL queries. For questions and 
comments, write to the author @Practic_old
"""
import sqlite3
from sqlite3 import Error

def execute_query(connection, query, params):
    """ 
    Функция для записи 
    в sql базу 
    connection : соединение с БД
    query: str строка запроса SQLite
    params: list параметры запроса
    """
    res = None
    cursor = connection.cursor()
    try:

        if len(params) > 0:

            cursor.execute(query, params)
            # res = cursor.fetchone() # fetchall()
        else:
            cursor.execute(query)
            res = cursor.fetchall()
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

    return res

def execute_query_select(connection, query, params):
    """ 
    Функция для чтения из sql базы 
    возвращает список кортежей 
    connection : соединение с БД
    query: str строка запроса SQLite
    params: list параметры запроса
    """
    res = None
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        res = cursor.fetchall()

        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

    return res

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
 
    return connection


class SQLiteDB():

    def __init__(self, DBNAME):
        self.DBNAME = DBNAME

    def create_table(self, table:str, list_query_params:list):
        connection = create_connection(self.DBNAME)
        """
        Функция для создания таблицы
        table: str имя таблицы
        list_query_params: list параметры запроса
        Пример как передаются имена столбцов в таблицу, списком кортежей
        list_query_params = [
        ('from_user_id', 'INTEGER UNIQUE'),     здесь должны быть уникальные значения
        ('from_user_username', 'TEXT'),
        ('from_user_firstname', 'TEXT'),
        ('regtime', 'INTEGER')
        ]
        """
        text_query=''
        for i in list_query_params:
            text_query += f"{i[0]} {i[1]},\n"
        text_query=text_query[:-2]  

        query = f"CREATE TABLE IF NOT EXISTS {table} ({text_query});"
        execute_query(connection=connection, query=query, params=[])
        connection.close()

    def find_elements_in_column(self, table_name:str, key_name:str, column_name:str):
        """
        функция поиска в базе данных 
        по значению ячейки с указанием имени колонки
        возвращает список кортежей одной строки таблицы
        table_name: str имя таблицы
        key_name: str имя колонки
        column_name: str имя ячейки
        """
        connection = create_connection(self.DBNAME)
        query = f"""SELECT * 
                FROM {table_name}
                WHERE {column_name} = ?
                """ 
        list_of_tuple = execute_query_select(connection, query=query, params=[key_name])
        connection.close()
        return list_of_tuple
    
    def find_elements_by_keyword(self, table_name:str, key_name:str, column_name:str):
        """
        функция поиска в базе данных 
        ищет совпадения в колонке по строке
        возвращает список кортежей
        table_name: str имя таблицы
        key_name: str имя колонки
        column_name: str имя ячейки
        """
        connection = create_connection(self.DBNAME)

        query = f"""SELECT * 
                FROM {table_name}
                WHERE {column_name} LIKE '%{key_name}%' 
                """ 
        print(query)
        list_of_tuple = execute_query_select(connection, query=query, params=[])
        connection.close()
        return list_of_tuple
    
    def upd_element_in_column(self, table_name:str, upd_par_name: str, key_par_name: str, upd_column_name: str, key_column_name:str):
        """
        функция обновления в базе данных 
        по значению ячейки с указанием имени колонки
        table_name: str имя таблицы
        upd_par_name: str имя параметра для обновления
        key_par_name: str имя параметра для поиска
        upd_column_name: str имя колонки для обновления
        key_column_name: str имя колонки для поиска
        """
        connection = create_connection(self.DBNAME)
        query = f"""
            UPDATE {table_name}
            SET {upd_par_name} = ?
            WHERE {upd_column_name} = ?
            """
        print(query)
        execute_query(connection, query=query, params=[key_par_name, key_column_name])
        connection.close()
    
    def ins_unique_row(self, table_name:str, list_query_params:list):
        """
        функция вставки строчки в базу данных 
        уникального значения с указанием имени колонки
        если был флаг UNIQUE при создании колонки в таблице БД
        table_name: str имя таблицы
        list_query_params: list список кортежей одной строки таблицы
        Пример загрузки списка параметров 
        list_query_params = [
        ('from_user_id', '123'),
        ('from_user_username', 'vasya'),
        ('from_user_firstname', 'petrov'),
        ('regtime', '1234568')
        ]   
        """
        connection = create_connection(self.DBNAME)

        text_params=''
        for i in list_query_params:
            text_params += f"{i[0]},\n"
        text_params=text_params[:-2]  

        list_value = []
        text_questions = ""
        for i in list_query_params:
            list_value.append(i[1])
            text_questions += f"?,"
        text_questions=text_questions[:-1] 

        query = """
        INSERT OR IGNORE INTO {table} ({text_params}) VALUES ({text_questions})
        """.format(table=table_name, text_params=text_params, text_questions=text_questions)

        execute_query(connection=connection, query=query, params=list_value)
        connection.close()

        connection.close()

# def main():
#     db=SQLiteDB('users.db')
#     list_query_params = [
#     ('from_user_id', '123'),
#     ('from_user_username', 'vasya'),
#     ('from_user_firstname', 'petrov'),
#     ('regtime', '1234568')
#     ]   
#     # db.ins_unique_row(table_name='users', list_query_params=list_query_params)
#     res = db.find_elements_by_keyword(table_name='users', key_name='2023-06', column_name='reg_data')

#     for i in res:
#         print(str(i)+'\n')
# if __name__ == "__main__":
#     main()

