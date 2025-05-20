import pymysql

class DatabaseWrapper:
    def __init__(self, host, user, port, password, database):
        self.db_config = {
            "host": host,
            "user": user,
            "port": port,
            "password": password,
            "database": database,
            "cursorclass": pymysql.cursors.DictCursor
        }
        self.create_table()

    def connect(self):
        return pymysql.connect(**self.db_config)

    def execute_query(self, query, params=()):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
        conn.close()
    
    def fetch_query(self, query, params=()):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        conn.close()
        return result

    def create_table(self):
        self.execute_query('''
            CREATE TABLE IF NOT EXISTS listaSpesa(
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL
            )
        ''')

    def aggiungi_elemento(self, nome):
        self.execute_query('INSERT INTO listaSpesa (nome) VALUES (%s)', (nome))

    def get_elemento(self):
        return self.fetch_query('SELECT * FROM listaSpesa')

    def rimuovi_elemento(self, index):
        return self.execute_query('DELETE FROM listaSpesa WHERE id=(%s)', (index))