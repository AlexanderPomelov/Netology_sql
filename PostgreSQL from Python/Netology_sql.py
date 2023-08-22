import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE IF NOT EXISTS client (
                client_id SERIAL PRIMARY KEY,
                first_name VARCHAR(60) NOT NULL,
                last_name VARCHAR(60) NOT NULL,
                email VARCHAR(60) UNIQUE NOT NULL);
                 """)
        conn.commit()
        cur.execute("""
                CREATE TABLE IF NOT EXISTS phone (
                phone_id SERIAL PRIMARY KEY,
                client_id INTEGER REFERENCES client(client_id),
                phone_number VARCHAR(60));
                """)
        conn.commit()
        print(f'Таблицы созданы')

def add_client(conn, first_name, last_name, email, phone_number = None):
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO client (first_name, last_name, email)
                    VALUES (%s, %s, %s)
                    RETURNING client_id, first_name, last_name, email;""",
                    (first_name, last_name, email))
        conn.commit()
        return print(cur.fetchall())

def add_phone(conn, client_id, phone_number):
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO phone (client_id, phone_number)
                    VALUES (%s, %s)
                    RETURNING client_id, phone_number;""",
                    (client_id, phone_number))
        conn.commit()
        return print(cur.fetchall())

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phone_number=None):
    with conn.cursor() as cur:
        cur.execute("""UPDATE client SET first_name = %s, last_name = %s, email = %s WHERE client_id = %s;
                    """,
                    (first_name, last_name, email, client_id))
        conn.commit()
        cur.execute("""SELECT * FROM client
                               WHERE client_id=%s""",
                    (client_id,))
        return print(cur.fetchall())

def delete_phone(conn, client_id, phone_number):
    with conn.cursor() as cur:
        cur.execute(""" DELETE FROM phone WHERE client_id = %s;""",
                    (client_id,))
        conn.commit()
        print('Телефон удален')

def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute(""" DELETE FROM client WHERE client_id = %s;""",
                    (client_id))
        conn.commit()
        print('Клиент удален')

def find_client(conn, first_name=None, last_name=None, email=None, phone_number=None):
    with conn.cursor() as cur:
        cur.execute("""SELECT client_id FROM client
                        JOIN phone USING (client_id)
                        WHERE first_name = %s AND last_name = %s AND email = %s AND phone_number = %s;
                        """,
                    (first_name, last_name, email, phone_number))
        conn.commit()
        print(cur.fetchall())

def delete_table(conn):
    with conn.cursor() as cur:
        cur.execute("""DROP TABLE phone; 
                    DROP TABLE client;""")
        conn.commit()
        print('Таблицы удалены')


if __name__ == '__main__':
    conn = psycopg2.connect(database = 'netology_db', user = 'postgres', password = '')
    create_db(conn)
    add_client(conn, 'John', 'Bradley', 'johnbradley@gmail.com')
    add_client(conn, 'Иван', 'Петрович', 'ivan.petrovich@gmail.com')
    add_phone(conn, 3, '123455555')
    add_phone(conn, 2, '111111111')
    change_client(conn, 3, 'Alexey', 'Skorov', 'alexey.skorov@gmail.com')
    delete_phone(conn, 1, '123455555')
    delete_client(conn, '1')
    find_client(conn, 'Alexey', 'Skorov', 'alexey.skorov@gmail.com', '123455555')

    delete_table(conn)
    conn.close()
