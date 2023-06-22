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
    Function for recording
    to sql database
    connection : database connection
    query: str SQLite query string
    params: list request parameters
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
    Function for reading from sql database
    returns a list of tuples
    connection : database connection
    query: str SQLite query string
    params: list request parameters
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
        Function to create a table
        table: str table name
        list_query_params: list query parameters
        An example of how column names are passed to a table by a list of tuples
        list_query_params = [
        ('from_user_id', 'INTEGER UNIQUE'),   must be unique values ​​here
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
        database search function
        by cell value with column name
        returns a list of tuples of one table row
        table_name: str table name
        key_name: str key name
        column_name: str column name
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
        database search function
        searches for matches in a column line by line
        returns a list of tuples
        table_name: str the name of the table
        key_name: str keyword string
        column_name: str column name
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
        database update function
        by cell value with column name
        table_name: str table name
        upd_par_name: str name of the parameter to update
        key_par_name: str name of the parameter to search
        upd_column_name: str name of the column to update
        key_column_name: str name of the column to search
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
        database insertion function
        unique value with column name
        if there was a UNIQUE flag when creating 
        a column in a database table
        table_name: str table name
        list_query_params: list list of tuples of one table row
        Parameter List Loading Example 
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
#     db.ins_unique_row(table_name='users', list_query_params=list_query_params)
#     res = db.find_elements_by_keyword(table_name='users', key_name='2023-06', column_name='reg_data')

#     for i in res:
#         print(str(i)+'\n')
# if __name__ == "__main__":
#     main()

