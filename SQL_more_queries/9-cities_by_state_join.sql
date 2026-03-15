-- 'hbtn_0d_usa' bazasındakı bütün şəhərləri və onlara uyğun ştat adlarını siyahılayır.
-- 'cities.id', 'cities.name' və 'states.name' sütunlarını göstərir.
-- Nəticələr cities.id-yə görə artan sıra ilə düzülür.

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
