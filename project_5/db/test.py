import sqlite3
def sql_con():
    con = sqlite3.connect('testdb.db')
    cs = con.cursor()
    rs = cs.execute('SELECT * FROM student_table;')
    result =""
    for row in rs:
        result  = result +  row[0]+ '\n'
    print(result)
    con.close()
sql_con()