-- 'force_name' cədvəlini yaradır.
-- id: INT
-- name: VARCHAR(256), NULL ola bilməz (NOT NULL).
-- Əgər cədvəl artıq mövcuddursa, skript xəta vermir.

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
