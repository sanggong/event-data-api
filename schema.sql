CREATE TABLE events (
	id BIGINT NOT NULL,
	user_id BIGINT NOT NULL,
	event ENUM('login', 'stagein', 'clear', 'fail', 'purchase') NOT NULL,
	event_datetime DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (id),
	INDEX idx_user (user_id)
) ENGINE=InnoDB
DEFAULT CHARSET=utf8;

CREATE TABLE purchases (
	id BIGINT NOT NULL,
	event_id BIGINT NOT NULL,
	currency ENUM('krw', 'usd') DEFAULT 'krw' NOT NULL,
	price BIGINT NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (event_id),
	CONSTRAINT fk_purchases_to_events
		FOREIGN KEY (event_id) REFERENCES events (id)
		ON DELETE RESTRICT
		ON UPDATE RESTRICT
) ENGINE=InnoDB
DEFAULT CHARSET=utf8;

CREATE TABLE stages (
	id BIGINT NOT NULL AUTO_INCREMENT,
	event_id BIGINT NOT NULL,
	stage INT NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (event_id),
	CONSTRAINT fk_stages_to_events
		FOREIGN KEY (event_id) REFERENCES events (id)
		ON DELETE RESTRICT
		ON UPDATE RESTRICT
) ENGINE=InnoDB
DEFAULT CHARSET=utf8;

