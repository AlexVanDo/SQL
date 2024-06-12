import psycopg2

def createdb(basename, username, password):
    connection = psycopg2.connect(user=username, password=password)
    cursor = connection.cursor()
    connection.autocommit = True
    cdbsql = f'CREATE DATABASE {basename}'
    cursor.execute('CREATE DATABASE %s', (basename,))
    cursor.close()
    connection.close()

def create_tabels():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Clients
                   (id SERIAL PRIMARY KEY,
                   first_name VARCHAR(60) NOT NULL,
                   last_name VARCHAR(60) NOT NULL,
                   email VARCHAR(60) UNIQUE NOT NULL);
                   """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS Phone_numbers 
                   (id SERIAL PRIMARY KEY, 
                   client_id INTEGER NOT NULL REFERENCES Clients(id), 
                   phone_number VARCHAR(60) UNIQUE NOT NULL);
                   """)

def new_client(first_name, lastname, email, numbers=None):
    sql = (f'''INSERT INTO Clients(first_name, last_name, email) 
                   VALUES(%s, %s, %s)
           ON CONFLICT (email) DO NOTHING;
                   ''')
    vel = (first_name, lastname, email)
    cursor.execute(sql, vel)
    sql = ('SELECT id FROM Clients WHERE email LIKE %s;')
    vel = (email, )
    cursor.execute(sql, vel)
    client_id = cursor.fetchone()[0]

    sql = (f'''INSERT INTO Phone_numbers(client_id, phone_number) 
           VALUES(%s, %s)
           ON CONFLICT DO NOTHING
           ''')
    if bool(numbers) is True:    
        for number in numbers:
            vel = (client_id, number)
            cursor.execute(sql, vel)

def new_number(client_id, number):
    sql = '''INSERT INTO Phone_numbers(client_id, phone_number) 
            VALUES(%s, %s)
            ON CONFLICT DO NOTHING
    '''
    vel = (client_id, number)
    cursor.execute(sql, vel)

def change_client(client_id, first_name=None, last_name=None, email=None, numbers=None):
    client_data = [first_name, last_name, email, numbers]
    for data in client_data:
        if data and type(data) is not list:
            if data == first_name:     
                sql = 'UPDATE Clients SET first_name=%s WHERE id=%s;'
                vel = (first_name, client_id)
                cursor.execute(sql, vel)   
            elif data == last_name:     
                sql = 'UPDATE Clients SET last_name=%s WHERE id=%s;'
                vel = (last_name, client_id)
                cursor.execute(sql, vel)
            elif data == email:     
                sql = 'UPDATE Clients SET email=%s WHERE id=%s;'
                vel = (email, client_id)
                cursor.execute(sql, vel)
        elif type(data) is list:
            for number in data:
                    sql = '''INSERT INTO Phone_numbers(client_id, phone_number) 
                        VALUES(%s, %s)
                        ON CONFLICT DO NOTHING
                    '''
                    vel = (client_id, number)
                    cursor.execute(sql, vel)           

def delete_phone(client_id, number):
    sql = 'DELETE FROM phone_numbers WHERE client_id=%s AND phone_number=%s;'
    vel = (client_id, number)
    cursor.execute(sql, vel)

def delete_client(client_id):
    cursor.execute('DELETE FROM phone_numbers WHERE client_id=%s;', (client_id,))
    cursor.execute('DELETE FROM clients WHERE id=%s;', (client_id,))

def find_client(first_name=None, last_name=None, email=None, number=None):
    client_data = [first_name, last_name, email, number]
    for data in client_data:
        if data and type(data):
            if data == first_name:     
                sql = 'SELECT * FROM Clients WHERE first_name=%s;'
                vel = (first_name,)
                cursor.execute(sql, vel)
                print(cursor.fetchall())
            elif data == last_name:     
                sql = 'SELECT * FROM Clients WHERE last_name=%s;'
                vel = (last_name,)
                cursor.execute(sql, vel)
                print(cursor.fetchall())
            elif data == email:     
                sql = 'SELECT * FROM Clients WHERE email=%s;'
                vel = (email,)
                cursor.execute(sql, vel)
                print(cursor.fetchall())
            elif data == number:
                sql = '''SELECT * FROM Clients c
                    JOIN phone_numbers pn ON c.id = pn.client_id
                    WHERE pn.phone_number=%s;'''
                vel = (number,)
                cursor.execute(sql, vel)
                print(cursor.fetchall())

# createdb('clients_db', 'postgres', 'postgres')

with psycopg2.connect(database='clients_db', user='postgres', password='postgres') as conn:
    cursor = conn.cursor()
    conn.autocommit = True

    # create_tabels()

    # new_client('Алан', 'Строуберри', 'alan@gmail.com', ['8767568756', '4353453646'])
    # new_client('Борис', 'Смирнов', 'borya@gmail.com', ['87658453632'])
    # new_client('Анатолий', 'Смирнов', 'ggggg@gmail.com', ['8434336','325436457', '234234'])

    # new_number('2', '8798756756')

    # change_client('2', 'Владислав', None, None, ['1242341145', '874646748754'])
    
    # delete_phone(3, '234234')
    
    # delete_client('3')

    # 4 разных клиента по 4м разным данным
    # find_client('Владислав', 'Строуберри', 'ggggg@gmail.com', '87658453632')

cursor.close()
conn.close()