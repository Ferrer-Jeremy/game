CREATE DATABASE crawler;
USE crawler;

-- PROXY

CREATE TABLE `crawler_overseer__proxy` (
  `id` INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `ip` VARCHAR(39) UNIQUE NOT NULL,
  `port` INT(5) NOT NULL,
  `user` VARCHAR(50) DEFAULT NULL,
  `password` VARCHAR(255) DEFAULT NULL,
  `source` VARCHAR(20) NOT NULL,
  `server` VARCHAR(40) NOT NULL,
  `last_response_time` DECIMAL(5,3) UNSIGNED,
  `last_time_used_at` DATETIME DEFAULT NULL,
  `enabled` TINYINT(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;


CREATE TABLE `crawler_overseer__proxy_blacklist` (
  `proxy_id` INT(6) UNSIGNED NOT NULL,
  `dealer_id` INT(3) NOT NULL,
  `blacklisted_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (proxy_id, dealer_id)
) ENGINE=InnoDB DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;


ALTER TABLE `crawler_overseer__proxy_blacklist` ADD CONSTRAINT FK_CO_PROXY_BLACKLIST FOREIGN KEY (proxy_id) REFERENCES `crawler_overseer__proxy` (id);

-- END PROXY

-- SPIDER

# CREATE TABLE `spider` (
#   `id_spider` INT(4) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
#   `name_dealer` varchar(255) NOT NULL,
#   `spider_mode` ENUM('stores', 'categories', 'products_list', 'products') NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;

CREATE TABLE `spider__run` (
  `id_run` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `spider_name` VARCHAR(255) NOT NULL,
  `start_time` DATETIME NOT NULL,
  `end_time` DATETIME NOT NULL,
  `end_state` ENUM('finished', 'shutdown') NOT NULL,
  `item_scraped` INT UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;

# ALTER TABLE `spider__run` ADD CONSTRAINT FK_SPIDER_RUN FOREIGN KEY (id_spider) REFERENCES `spider` (id_spider);

# CREATE TABLE `spider__error`(
#   `id_error` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
#   `id_run` INT UNSIGNED NOT NULL,
#   `level` ENUM('debug', 'info', 'warning', 'error', 'critical') NOT NULL,
#   `time` DATETIME NOT NULL,
#   `message` VARCHAR(511) NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;

# ALTER TABLE `spider__error` ADD CONSTRAINT FK_SPIDER_ERROR FOREIGN KEY (id_run) REFERENCES `spider__run` (id_run);

-- END SPIDER
