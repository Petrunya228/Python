import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
SELECT customer.full_name AS name_customer, manager.full_name AS name_manager, orderr.purchase_amount AS amount, orderr.date AS date
FROM orderr
JOIN customer ON orderr.customer_id = customer.manager_id
JOIN manager ON customer.manager_id = manager.manager_id
''')

result = cursor.fetchall()

for row in result:
    print(row)

conn.close()
