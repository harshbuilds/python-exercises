from conn import db_conn

conn = db_conn()
# query = "INSERT INTO arc.pub78orgs_test VALUES (101, 'Test Org', 'Testland', 'Testing', 'TestUniverse', 'Test');"

print("Enter (ein, org, city, state, country, type) to insert in table:")
data = list(map(lambda x: x.strip(), input().split(',')))
data[0] = int(data[0])

cursor = conn.cursor()
query = "INSERT INTO arc.pub78orgs_test VALUES (?, ?, ?, ?, ?, ?);"
cursor.execute(query, *data)
cursor.execute('SELECT * FROM arc.pub78orgs_test WHERE ein=?', data[0])

# 234, Hello, PyCity, PyState, PyCountry, PyType

records = cursor.fetchall()
for r in records:
    print(r)

conn.commit()
conn.close()
