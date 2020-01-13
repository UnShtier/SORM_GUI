from pandas import read_csv
from textwrap import wrap


def decode(row):
    return ''.join([chr(int(a, 16)) for a in wrap(row[2:], 2)])


def html_extractor(row):
    return row.split('<html>')[1].split('</html>')[0] if row.find('<html>') != -1 else ''


class HTMLWorker:
    html = []

    def __init__(self, file_path, client_ip=None, server_ip=None, begin_date=None, end_date=None):
        data = read_csv(file_path, encoding='ascii')
        #data = data[data["Direction"] == 1]
        #data = data[data["UserId"] == client_ip]
        #data = data[data["ServerId"] == server_ip]
        #data = data[data["Date"] in (begin_date, end_date)]
        self.html = data['Data'].apply(decode).apply(html_extractor).values.tolist()
        print(1)

    def get_html(self):
        print([s for s in self.html if s != ''])
        return [s for s in self.html if s != '']


