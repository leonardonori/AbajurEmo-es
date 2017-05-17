USE banco01;

CREATE TABLE words(
	id_word INT NOT NULL AUTO_INCREMENT,
	word VARCHAR(80) NOT NULL,
    equivalent INT NOT NULL COMMENT "1=>POSITIVE, -1=>NEGATIVE",
    PRIMARY KEY (id_word)
);

CREATE TABLE tweets(
	id_tweet DECIMAL(64,0) NOT NULL,
    tweet VARCHAR(142) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
	status DECIMAL(1,0) DEFAULT 0 COMMENT "0=>NOT ANALYZED, 1=> ANALYZED",
	PRIMARY KEY (id_tweet)
);

CREATE TABLE signal_status(
	id_signal INT NOT NULL AUTO_INCREMENT,
    signal_statustweets DECIMAL(1,0) DEFAULT 0 COMMENT "0=>neutral, 1=>positive, -1=>negative",
    PRIMARY KEY (id_signal)
);
