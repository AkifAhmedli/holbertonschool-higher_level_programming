-- 'second_table' cədvəlində eyni bala malik olan yazıları qruplaşdırır.
-- Hər bir balı (score) və həmin bala malik olanların sayını (number) göstərir.
-- Nəticə sayı ən çox olandan başlayaraq (descending) sıralanır.
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
