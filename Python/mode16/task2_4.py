import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
SELECT customer.full_name, orderr.order_no
FROM customer
JOIN orderr ON customer.customer_id = orderr.customer_id
WHERE orderr.manager_id = customer.manager_id
''')


result = cursor.fetchall()

for row in result:
    print(row)

conn.close()
