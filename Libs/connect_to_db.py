"""Helper Class to make the Database calls shorter."""

import psycopg2


class Connection():
    def __init__(self):
        self.connect = psycopg2.connect(database ="b4zcxz6bmhjsudbphroo",
                                      host="b4zcxz6bmhjsudbphroo-postgresql.services.clever-cloud.com",
                                      user="ucsuarf2fko8ds4k3443",
                                      password="W2JF95zE1czTx9ngxrZyX2nHxi3Drm",
                                      port="50013")