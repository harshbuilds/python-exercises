import pyodbc


def db_conn():
    server = 'tartarus-ml-server-exp.database.windows.net'
    database = 'ai-research-exp'
    login = 'arc_sh_readwrite_lg_01'
    password = '5at0doxO'
    conn_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={login};PWD={password}'
    conn = pyodbc.connect(conn_string)
    # query = "SELECT name FROM sys.tables"
    # cursor = conn.cursor()
    # cursor.execute(query)
    # records = cursor.fetchall()
    # for r in records:
    #     print(r)
    # print(conn)
    # conn.close()
    return conn
