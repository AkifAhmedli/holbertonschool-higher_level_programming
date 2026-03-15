-- 'hbtn_0d_tvshows' bazasında heç bir janra bağlanmamış serialları siyahılayır.
-- LEFT JOIN istifadə edərək bütün seriallar gətirilir,
-- sonra WHERE ilə yalnız janr ID-si NULL olanlar seçilir.
-- Nəticə serialın başlığına və janr ID-nə görə artan sıra ilə düzülür.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
