-- 'hbtn_0d_usa' bazasındakı California ştatına aid şəhərləri siyahılayır.
-- JOIN istifadə edilmir, alt-sorğu (subquery) tətbiq olunur.
-- Nəticələr cities.id-yə görə artan sıra ilə düzülür.

SELECT id, name 
FROM cities 
WHERE state_id = (
    SELECT id 
    FROM states 
    WHERE name = 'California'
) 
ORDER BY id ASC;
