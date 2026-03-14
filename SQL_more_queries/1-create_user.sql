-- 'user_0d_1' istifadəçisini 'user_0d_1_pwd' şifrəsi ilə yaradır.
-- Əgər istifadəçi artıq mövcuddursa, skript xəta vermir.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- İstifadəçiyə bütün server üzrə (*.*) tam səlahiyyətlər verir.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Dəyişikliklərin dərhal qüvvəyə minməsini təmin edir.
FLUSH PRIVILEGES;
