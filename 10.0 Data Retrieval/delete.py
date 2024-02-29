from conn import db_conn

conn = db_conn()

print("Enter ein of the record to delete: ", end="")
data = int(input())
query = "DELETE FROM arc.pub78orgs_test WHERE ein = ?";
cursor = conn.cursor()
cursor.execute(query, data)
print('{} Rows deleted!'.format(cursor.rowcount))
conn.commit()
conn.close()
