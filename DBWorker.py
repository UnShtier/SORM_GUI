import psycopg2 as p


class DBWorker:

    def __init__(self, ip, login, password):
        self._conn = p.connect(dbname='Keys', user=login, password=password, host=ip)
        self._cursor = self._conn.cursor()

    def __exit__(self):
        self._cursor.close()
        self._conn.close()

    def get_key(self, ip, port):
        self._cursor.execute("select get_key('" + ip + "', '" + port + "')")
        return self._cursor.fetchall()

    def put_key(self, raw_cert, ip, port, private_key):
        self._cursor.execute("select put_certificate"
                             "('" + raw_cert + "', '" + ip + "', '" + port + "', '" + private_key + "')")


