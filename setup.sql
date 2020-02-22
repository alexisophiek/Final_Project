-- drop table if exists twitter_feed;
CREATE TABLE twitter_feed (
	date TIMESTAMP,
	user_location  TEXT,
	user_id TEXT,
	text TEXT,
	metadata TEXT
);

-- drop table if exists tweets;
CREATE TABLE tweets (
	id BIGSERIAL PRIMARY KEY,
	data JSONB
);

-- drop table if exists tweet_impressions;
CREATE TABLE tweet_impressions  (
	id INT PRIMARY KEY NOT NULL, 
	username TEXT, 
	followers INT, 
	interactions INT
);