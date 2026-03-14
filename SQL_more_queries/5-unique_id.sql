-- 'unique_id' cədvəlini yaradır.
-- id: INT, standart dəyəri 1-dir və unikal (unique) olmalıdır.
-- name: VARCHAR(256).
-- Əgər cədvəl artıq mövcuddursa, skript xəta vermir.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
