import psycopg2 as p
import XmlWorker as xml


class DBWorker:

    def __init__(self, config_file):
        self.params = xml.XmlWorker(config_file).get_values()

    def init_keys_connection(self):
        self.keys = p.connect(user=self.params['key_database_login'], password=self.params['key_database_password'],
                              host=self.params['key_database_ip'], database='Keys')
        if self.keys:
            self.keys_cursor = self.keys.cursor()
            return 1
        else:
            return 0

    def close_keys(self):
        if self.keys:
            self.keys.close()
            self.keys_cursor.close()

    def __exit__(self):
        self.close_keys()

    def init_traffic_connection(self):
        self.traffic = p.connect(user=self.params['traffic_database_login'],
                                 password=self.params['traffic_database_password'],
                                 host=self.params['traffic_database_ip'], database='Keys')
        if self.traffic:
            self.traffic_cursor = self.keys.cursor()
            return 1
        else:
            return 0

    def close_traffic(self):
        if self.traffic:
            self.traffic.close()
            self.traffic_cursor.close()

    def get_key(self, ip, port):
        if self.keys:
            self.keys_cursor.execute("select get_key('" + ip + "', '" + port + "')")
            return self.keys_cursor.fetchall()
        else:
            return []

    def put_key(self, raw_cert, ip, port, private_key):
        if self.keys:
            self.keys_cursor.execute("select put_certificate"
                                     "('" + raw_cert + "', '" + ip + "', '" + port + "', '" + private_key + "')")
            return self.keys_cursor.fetchall()
        else:
            return [0]

    def read_certs(self):
        if self.keys:
            self.keys_cursor.execute("select cert_scan()")
            return self.keys_cursor.fetchall()
        else:
            return [0]

    def get_traffic(self, begin_date, end_date, client_ip, server_ip):
        pass
