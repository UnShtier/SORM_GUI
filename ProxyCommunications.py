import requests as r


class ProxyCommunications(object):
    proxy_connection = []

    def __init__(self, ip, ):
        self.output_query_buffer = []
        self.input_query_buffer = []

