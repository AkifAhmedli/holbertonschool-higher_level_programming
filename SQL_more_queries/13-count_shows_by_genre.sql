-- 'hbtn_0d_tvshows' bazasındakı janrları və onlara bağlı serialların sayını siyahılayır.
-- Yalnız ən azı bir serialı olan janrlar göstərilir.
-- Nəticələr serialların sayına görə azalan (DESC) sıra ilə düzülür.

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
