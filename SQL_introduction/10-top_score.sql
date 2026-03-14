-- 'second_table' cədvəlindəki bütün sətirləri siyahılayır.
-- Nəticələr 'score' və sonra 'name' sütunlarını göstərir.
-- Sətirlər 'score' sütununa görə azalan sıra ilə (yuxarıdan aşağı) düzülür.
SELECT score, name FROM second_table ORDER BY score DESC;
