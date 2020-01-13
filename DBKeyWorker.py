import psycopg2 as p
import XmlWorker as xml


class DBKeyWorker:

    def __init__(self, config_file):
        self.params = xml.XmlWorker(config_file).get_values()

    def init_keys_connection(self):
        self.keys = p.connect(user=self.params['key_database_login'], password=self.params['key_database_password'],
                             host=self.params['key_database_ip'], database='Keys')
        if self.keys:
            self.keys_cursor = self.keys.cursor()
        else:
            print('Connection to database Keys failed')

    def __exit__(self):
        self._cursor.close()
        self._conn.close()

    def get_key(self, ip, port):
        self._cursor.execute("select get_key('" + ip + "', '" + port + "')")
        return self._cursor.fetchall()

    def put_key(self, raw_cert, ip, port, private_key):
        self._cursor.execute("select put_certificate"
                             "('" + raw_cert + "', '" + ip + "', '" + port + "', '" + private_key + "')")

    def read_certs(self):
        self._cursor.execute("select cert_scan()")
        return self._cursor.fetchall()



