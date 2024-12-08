Для подготовки приложения необходимо выполнить следующие действия:

1. Создать виртуальное окружение:

	virtualenv venv


2. Активировать окружение:

	source venv/bin/activate

3. Установить пакеты flask, tinydb:

	pip install flask tinydb

Для запуска приложения выполнить команду:

	python app.py

Для запуска скрипта с тестовыми запросами:

	python send_post.py