-- 'second_table' cədvəlində Bob adlı şəxsin balını (score) 10-a yeniləyir.
-- Filtr olaraq 'id' deyil, yalnız 'name' sütunundan istifadə edilir.
UPDATE second_table SET score = 10 WHERE name = 'Bob';
