import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
SELECT customer.full_name
FROM customer
LEFT JOIN orderr ON customer.customer_id = orderr.customer_id
WHERE orderr.customer_id IS NULL;
''')

result = cursor.fetchall()

for row in result:
    print(row)

conn.close()
