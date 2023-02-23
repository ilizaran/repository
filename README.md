

Simple respository for your documents

# Install

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt


    sudo mysql -u root -p
    CREATE DATABASE repository CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON repository.* TO 'usuario'@'localhost';

    create file repository/.env

    DEBUG=1
    DJANGO_SECRET_KEY=18d)f3_y$raf+$-_3sy!=17xq6eqcuvxa7v_#u+(24134123
    IMAGEN_LOGO=http://web.com/image.jpg
    TITLE=My repository
    DESCRIPTION=Text
    FOOTER=My organization
    #Repository file public with ngingx 
    URL=http://localhost:9901/datos/

    MYSQL_PORT=3306
    MYSQL_USER=usuario
    MYSQL_PASSWORD=password
    MYSQL_DATABASE=repository
    MYSQL_HOST=localhost
