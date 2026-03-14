-- 'second_table' cədvəlində score >= 10 olan bütün sətirləri siyahılayır.
-- Nəticədə 'score' və 'name' sütunları göstərilir.
-- Sıralama 'score' sütununa görə azalan (yuxarıdan aşağı) qaydadadır.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
