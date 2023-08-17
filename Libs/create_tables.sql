-- This SQL code is for Deleting ALL data from all of the Tables in the Database and recreating them.
-- Do NOT use it unless you have Backed up the online database AND you know what your doing.

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
	"username"	VARCHAR(255) NOT NULL,
	"senior"	BOOLEAN NOT NULL,
	"timestamp"	TIMESTAMP NOT NULL,
	PRIMARY KEY("annotation_id"),
	FOREIGN KEY("username") REFERENCES "users"("username")
);

DROP TABLE IF EXISTS review CASCADE;
CREATE TABLE "review" (
	"review_id"	BIGSERIAL NOT NULL,
	"annotation_id"	INTEGER NOT NULL,
	"reviewer"	VARCHAR(255) NOT NULL,
	"review_decision"	BOOLEAN NOT NULL,
	"review_comment"	TEXT,
	"new_class"	VARCHAR(255) NOT NULL,
	"new_confidence"	INTEGER NOT NULL,
	"new_comment"	TEXT,
	"timestamp"	TIMESTAMP NOT NULL,
	PRIMARY KEY("review_id"),
	FOREIGN KEY("annotation_id") REFERENCES "annotation"("annotation_id"),
	FOREIGN KEY("reviewer") REFERENCES "users"("username")
);

DROP VIEW annotation_review;
CREATE VIEW annotation_review AS
SELECT a.annotation_id, a.path, a.class, a.confidence, a.comment, a.username, a.senior, a.timestamp AS annotation_timestamp, r.review_id, r.reviewer, r.review_score, r.review_comment, r.new_class, r.new_confidence, r.new_comment, r.timestamp AS review_timestamp
FROM annotation a
JOIN review r ON a.annotation_id = r.annotation_id;
