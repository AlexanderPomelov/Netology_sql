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
        cur.execute("""
                CREATE TABLE IF NOT EXISTS phone (
                phone_id SERIAL PRIMARY KEY,
                client_id INTEGER REFERENCES client(client_id),
                phone_number VARCHAR(60));
                """)
        print(f'Таблицы созданы')

def add_client(conn, first_name, last_name, email, phone_number = None):
    with conn.cursor() as cur:
        cur.execute("""
                    INSERT INTO client (first_name, last_name, email)
                    VALUES (%s, %s, %s)
                    RETURNING client_id, first_name, last_name, email;
                    """, (first_name, last_name, email))
        return print(cur.fetchall())

def add_phone(conn, client_id, phone_number):
    with conn.cursor() as cur:
        cur.execute("""
                    INSERT INTO phone (client_id, phone_number)
                    VALUES (%s, %s)
                    RETURNING client_id, phone_number;
                    """, (client_id, phone_number))
        return print(cur.fetchall())

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phone_number=None):
    with conn.cursor() as cur:
        if first_name is not None:
            cur.execute("""
                        UPDATE client SET first_name = %s WHERE client_id = %s;
                        """, (first_name, client_id))
        if last_name is not None:
            cur.execute("""
                        UPDATE client SET last_name = %s WHERE client_id = %s;
                        """, (last_name, client_id))
        if email is not None:
            cur.execute("""
                        UPDATE client SET email = %s WHERE client_id = %s;
                        """, (email, client_id))
        if phone_number is not None:
            cur.execute("""
                        UPDATE phone SET phone_number = %s WHERE client_id = %s;
                        """, (phone_number, client_id))
            cur.execute("""
                        SELECT * FROM client
                        JOIN phone USING (client_id)
                        WHERE client_id=%s;
                        """, (client_id,))
        return print(cur.fetchall())

def delete_phone(conn, client_id, phone_number):
    with conn.cursor() as cur:
        cur.execute("""
                    DELETE FROM phone WHERE client_id = %s;
                    """, (client_id,))
        print('Телефон удален')

def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""
                    DELETE FROM phone WHERE client_id = %s;
                    """, (client_id))
        cur.execute("""
                    DELETE FROM client WHERE client_id = %s;
                    """, (client_id))
        print('Клиент удален')

def find_client(conn, first_name=None, last_name=None, email=None, phone_number=None):
    with conn.cursor() as cur:
        if phone_number is not None:
            cur.execute("""
                        SELECT client_id FROM client
                        JOIN phone USING (client_id)
                        WHERE phone_number LIKE %s;
                        """, (phone_number,))
        else:
            cur.execute("""SELECT client_id FROM client
                        WHERE first_name ILIKE %s OR last_name ILIKE %s OR email LIKE %s;
                        """, (first_name, last_name, email))
        print(cur.fetchall())

def delete_table(conn):
    with conn.cursor() as cur:
        cur.execute("""DROP TABLE phone;
                    DROP TABLE client;""")
        print('Таблицы удалены')


if __name__ == '__main__':
    with psycopg2.connect(database = 'netology_db', user = 'postgres', password = '') as conn:
        #Создание таблицы
        create_db(conn)
        #Добавление клиентов
        add_client(conn, 'John', 'Bradley', 'johnbradley@gmail.com')
        add_client(conn, 'Иван', 'Петрович', 'ivan.petrovich@gmail.com')
        #Добавление номера телефона
        add_phone(conn, 1, '123455555')
        add_phone(conn, 2, '111111111')
        #Изменение данных клиента
        change_client(conn, 1, 'jon')
        change_client(conn, 1, None, 'Peter')
        change_client(conn, 1, None, None, 'asdfsdfa@asda.com')
        change_client(conn, 1, None, None, None, '11145678000')
        #Удаление телефона
        delete_phone(conn, 1, '123455555')
        #Удаление клиента
        delete_client(conn, '1')
        #Поиск клиента
        find_client(conn, 'Иван')
        find_client(conn, None, 'Петрович')
        find_client(conn, None, None, 'ivan.petrovich@gmail.com')
        find_client(conn, None, None, None, '111111111')
        #Удаление таблиц
        delete_table(conn)

