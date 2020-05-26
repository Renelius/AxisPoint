# Задание для AxisPoint

## Описание решения

   Первое задание "Получить данные по ссылке и загрузить их в БД", выполняет файл parse_json.py
предварительно создав модель Items в БД. Первый пункт второго задания выполнен двумя способами:
1. функцией items которая обрабатывает POST форму и отправляет JSON данные за определенный период;
2. функцией items_ajax, которая при загрузке HTML страницы сразу отправляет AJAX запрос(GET), получает
все данные и представляет их в виде списка ul в читаемом формате. Так же можно отфильтровать данные
по дате отправив AJAX (POST) запрос с нужными данными. Обработкой AJAX запросов занимается функция
ajax_response.

Второй пункт второго задания выполняется функцией send_xml, которая принимает данные о нужном
периоде, и отправляет exel файл с данными за этот период.


## Установка

В виртуальном окружении (virtualenv) выполнить данную команду:
```
pip install -r requirements.txt
```
Далее запустить сервер командой:
```
python manage.py runserver
```
или
```
./manage.py runserver
```


## Автор

* **Толстых Кирилл**
