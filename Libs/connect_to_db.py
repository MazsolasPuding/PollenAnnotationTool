"""Helper Class to make the Database calls shorter."""

import psycopg2


class Connection():
    def __init__(self):
        self.connect = psycopg2.connect(database ="bql3duq2x8p5l7r5ahz0",
                                      host="bql3duq2x8p5l7r5ahz0-postgresql.services.clever-cloud.com",
                                      user="ucsuarf2fko8ds4k3443",
                                      password="W2JF95zE1czTx9ngxrZyX2nHxi3Drm",
                                      port="5432")