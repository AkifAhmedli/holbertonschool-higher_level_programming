-- 'hbtn_0d_tvshows' bazasındakı serialları və onlara bağlı janr ID-lərini siyahılayır.
-- Yalnız ən azı bir janrı olan seriallar göstərilir.
-- Nəticə serialın başlığına və janr ID-nə görə artan sıra ilə düzülür.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
