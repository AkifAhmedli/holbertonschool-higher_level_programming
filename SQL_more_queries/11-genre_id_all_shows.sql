-- 'hbtn_0d_tvshows' bazasındakı bütün serialları və janr ID-lərini siyahılayır.
-- Janrı olmayan seriallar üçün NULL göstərilir.
-- Nəticələr başlıq (title) və janr ID-sinə görə artan sıra ilə düzülür.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
