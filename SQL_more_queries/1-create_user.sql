-- 'user_0d_1' istifadəçisini yaradır (əgər yoxdursa)
-- Şifrəni 'user_0d_1_pwd' olaraq təyin edir
-- Serverdəki bütün icazələri (privileges) verir
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
