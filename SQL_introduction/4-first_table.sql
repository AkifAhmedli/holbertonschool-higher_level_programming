-- Cari verilənlər bazasında 'first_table' adlı cədvəli yaradır.
-- Cədvəlin strukturu: id (tam ədəd) və name (256 simvola qədər mətn).
-- Əgər cədvəl artıq mövcuddursa, skript xəta vermədən tamamlanır.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
