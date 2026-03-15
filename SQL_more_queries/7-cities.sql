-- 'hbtn_0d_usa' bazasını yaradır və 'cities' cədvəlini əlavə edir.
-- 'cities' struktur:
--    id: INT, unikal, avtomatik artan, NULL ola bilməz, PRIMARY KEY.
--    state_id: INT, NULL ola bilməz, FOREIGN KEY (states.id-yə istinad edir).
--    name: VARCHAR(256), NULL ola bilməz.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
