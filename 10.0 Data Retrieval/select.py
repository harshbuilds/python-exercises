from conn import db_conn

conn = db_conn()
query = "SELECT TOP 100 * FROM arc.pub78orgs_test WHERE Type <> 'PC' ORDER BY Type DESC, Organization_Name;"
cursor = conn.cursor()
cursor.execute(query)
records = cursor.fetchall()
for r in records:
    print(r)

conn.close()
