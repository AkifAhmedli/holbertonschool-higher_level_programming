-- 'second_table' cədvəlindəki bütün sətirləri siyahılayır.
-- Adı (name) olmayan sətirləri nəzərə almır.
-- Nəticələr 'score' və 'name' ardıcıllığı ilə göstərilir.
-- Ballara görə azalan sıra ilə (yuxarıdan aşağı) düzülür.
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
