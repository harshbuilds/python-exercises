from conn import db_conn

conn = db_conn()

print("Enter state name for test_data: ", end="")
data = input()
query = "UPDATE arc.pub78orgs_test SET state = ? WHERE Type = 'Test'";
cursor = conn.cursor()
cursor.execute(query, data)
cursor.execute('SELECT * FROM arc.pub78orgs_test WHERE state = ?', data)
records = cursor.fetchall()
for r in records:
    print(r)

conn.commit()
conn.close()
