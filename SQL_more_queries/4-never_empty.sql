-- 'id_not_null' cədvəlini yaradır.
-- id: INT, standart (default) dəyəri 1-dir.
-- name: VARCHAR(256).
-- Əgər cədvəl artıq mövcuddursa, skript xəta vermir.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
