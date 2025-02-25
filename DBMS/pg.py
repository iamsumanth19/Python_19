import mysql.connector
import mysql.connector.cursor
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pg"
)
print('successfull!!')

cursor=connection.cursor()

query="""INSERT INTO persons (pid, pname, page, phone, date)
VALUES
(1, 'John Doe', 25, '9876543210', '2025-02-17'),
(2, 'Jane Smith', 30, '9876543211', '2025-02-17'),
(3, 'Alice Johnson', 22, '9876543212', '2025-02-17'),
(4, 'Bob Brown', 35, '9876543213', '2025-02-17'),
(5, 'Charlie Davis', 28, '9876543214', '2025-02-17'),
(6, 'David Wilson', 40, '9876543215', '2025-02-17'),
(7, 'Eve Martin', 29, '9876543216', '2025-02-17'),
(8, 'Frank Thomas', 33, '9876543217', '2025-02-17'),
(9, 'Grace Lee', 26, '9876543218', '2025-02-17'),
(10, 'Henry Clark', 38, '9876543219', '2025-02-17');"""

# cursor.execute(query)

# connection.commit()

cursor.execute("select * from persons")
result=cursor.fetchall()
for i in result:
    print(i)




