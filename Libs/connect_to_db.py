import psycopg2


class Connection():
    def __init__(self):
        self.connect = psycopg2.connect(database ="bql3duq2x8p5l7r5ahz0",
                                      host="bql3duq2x8p5l7r5ahz0-postgresql.services.clever-cloud.com",
                                      user="ucsuarf2fko8ds4k3443",
                                      password="W2JF95zE1czTx9ngxrZyX2nHxi3Drm",
                                      port="5432")

    def recreate_table(self):
        self.query = """
        DROP TABLE IF EXISTS users CASCADE;
        CREATE TABLE "users" (
        	"username"	VARCHAR(255) NOT NULL,
        	"password"	VARCHAR(255) NOT NULL,
        	"senior"	BOOLEAN NOT NULL,
        	PRIMARY KEY("username")
        );

        DROP TABLE IF EXISTS annotation CASCADE;
        CREATE TABLE "annotation" (
        	"annotation_id"	BIGSERIAL NOT NULL,
        	"path"	TEXT NOT NULL,
        	"class"	VARCHAR(255) NOT NULL,
        	"confidence"	INTEGER NOT NULL,
        	"comment"	TEXT,
        	"user"	VARCHAR(255) NOT NULL,
        	"senior"	BOOLEAN NOT NULL,
        	"timestamp"	TIMESTAMP NOT NULL,
        	PRIMARY KEY("annotation_id"),
        	FOREIGN KEY("user") REFERENCES "users"("username")
        );

        DROP TABLE IF EXISTS review CASCADE;
        CREATE TABLE "review" (
        	"review_id"	BIGSERIAL NOT NULL,
        	"annotation_id"	INTEGER NOT NULL,
        	"reviewer"	VARCHAR(255) NOT NULL,
        	"review_score"	INTEGER NOT NULL,
        	"review_comment"	TEXT,
        	"new_class"	VARCHAR(255) NOT NULL,
        	"new_confidence"	INTEGER NOT NULL,
        	"new_comment"	TEXT,
        	"timestamp"	TIMESTAMP NOT NULL,
        	PRIMARY KEY("review_id"),
        	FOREIGN KEY("annotation_id") REFERENCES "annotation"("annotation_id"),
        	FOREIGN KEY("reviewer") REFERENCES "users"("username")
        );
        """

        print(self.connection)
        cursor = self.connection.cursor()
        cursor.execute(self.query)
        # data = cursor.fetchall()
        self.connection.commit()
        self.connection.close()
