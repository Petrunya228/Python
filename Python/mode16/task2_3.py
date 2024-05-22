import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
SELECT orderr.order_no, manager.full_name, customer.full_name
FROM orderr
JOIN manager ON manager.manager_id = manager.manager_id
JOIN customer ON orderr.customer_id = customer.customer_id
WHERE manager.city <> customer.city;
''')


result = cursor.fetchall()

for row in result:
    print(row)

conn.close()
