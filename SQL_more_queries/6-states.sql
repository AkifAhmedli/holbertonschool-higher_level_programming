-- 'hbtn_0d_usa' bazasını və daxilində 'states' cədvəlini yaradır.
-- 'states' struktur:
--    id: INT, unikal, avtomatik artan, NULL ola bilməz və PRIMARY KEY-dir.
--    name: VARCHAR(256), NULL ola bilməz.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
