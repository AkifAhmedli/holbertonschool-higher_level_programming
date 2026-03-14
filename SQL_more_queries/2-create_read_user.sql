-- 'hbtn_0d_2' bazasını yaradır (əgər yoxdursa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- 'user_0d_2' istifadəçisini yaradır (əgər yoxdursa)
-- Şifrəni 'user_0d_2_pwd' olaraq təyin edir
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- İstifadəçiyə yalnız 'hbtn_0d_2' bazası üzərində SELECT hüququ verir
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
