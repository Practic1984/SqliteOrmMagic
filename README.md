# SqliteOrmMagic
 Facilitates the complex syntax of SQL queries through the use of standard commands for reading / writing to the SQlite3 database in Python program
**********************
<b>For example:</b><br>
<br>
Import<br>
<code>from SqliteOrmMagic import SQLiteDB</code><br>
<br>

<b>Importing the library:</b><br>
<code>import SqliteOrmMagic as som</code><br>
<br>
<b>Create an instance of the class:</b><br>
<code>db=som.SQLiteDB('users.db')</code><br>
<br>
<b>Create a table:</b><br>
<code>db.create_table(table, list_query_params)</code><br>
table: str table name <br>
list_query_params: list query parameters <br>
An example of how column names are passed to a table by a list of tuples:<br>
<code>list_query_params = [<br>
('from_user_id', 'INTEGER UNIQUE'),   must be unique values ​​here<br>
('from_user_username', 'TEXT'),<br>
('from_user_firstname', 'TEXT'),<br>
('regtime', 'INTEGER')<br>
]</code><br>
<br>
<b>Search in a column by cell value</b><br>
<code>res = db.find_elements_in_column(table_name, key_name, column_name)<br>
print(res) # print the search result</code><br>
Database search function by cell value with column name returns a list of tuples of one table row<br>
table_name: str table name<br>
key_name: str key name<br>
column_name: str column name<br>
<br>
<b>Search in a column by a string in a cell</b><br>
<code>res = db.find_elements_by_keyword(table_name, key_name, column_name)<br>
print(res) # print the search result</code><br>
Database search function searches for matches in a column line by line returns a list of tuples<br>
table_name: str the name of the table<br>
key_name: str keyword string<br>
column_name: str column name<br>
<br>
<b>Insert row with unique value by column</b><br>
<code>db.ins_unique_row(table_name, list_query_params)</code><br>
database insertion function unique value with column name if there was a UNIQUE flag when creating a column in a database table<br> 
table_name: str table name<br>
list_query_params: list list of tuples of one table row<br>
Parameter List Loading Example<br> 
<code>list_query_params = [<br>
('from_user_id', '123'),<br>
('from_user_username', 'vasya'),<br>
('from_user_firstname', 'petrov'),<br>
('regtime', '1234568')<br>
]</code><br>   
<br>
<b>Update the value of a cell in a column</b><br>
<code>db.upd_element_in_column(table_name, upd_par_name, key_par_name, upd_column_name, key_column_name)</code><br>
database insertion function unique value with column name if there was a UNIQUE flag when creating a column in a database table<br> 
database update function by cell value with column name<br>
table_name: str table name<br>
upd_par_name: str name of the parameter to update<br>
key_par_name: str name of the parameter to search<br>
upd_column_name: str name of the column to update<br>
key_column_name: str name of the column to search<br>
*********************
<b>all wishes and suggestions can be sent to the author @Practic_old</b>



