# RCon  minecraft  vk  bot
 
 

Вы можете удалённо управлять своим сервером даже с телефона.

Он отлично подойдёт для приватных серверов.


Видео-обзор №1 - youtube.com/watch?v=ZcsNEYVrbRY

Видео-обзор №2 - скоро....

Как установить ?

У вас должен быть python версии 3.8.0+


Установите из requirements.txt библиотеки.

pip install vk_api

pip install mcipc


Установите папку "RCon-bot"

Зайдите в файл rcnonbotc.py 

Вам нужно создать группу в ВК.

Подключите long poll версии 5.92

И получите токен для работы с API

На 12 строчке замените "token", на ваш токен.

На 19 строчке замените id, на id вашей группы.

Далее на 66 строчке в adminlist, вам нужно через запятую указать id админов. 

Далее подключаемся к RCon.

68 строчка.

'ip' заменяем на ip, port - на порт. И на 69 строчке 'password', на ваш пароль для RCon.

Убедитесь, что включили RCon!

