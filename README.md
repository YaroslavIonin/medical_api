#  Проектирование и реализация REST-API информационной системы районной поликлиники. Учет льготных лекарств.

## Описание проекта
1. API реализовано с помощью Django Rest Framework
2. Рабочая папка проекта server/
3. Приложение apps/medical:
- models/ отвечает за описание моделей (таблиц БД) проекта
- admin/ отвечает за описание моделей в django админке 
- serializers/ отвечает за обработку объектов python в формат JSON и обратно, валидацию данных
- viewsets/ отвечает за логику программы при обращении к API
- routers.py собирает все эндпоинты к апи
4. Модуль config/ - настройки проекта
5. БД sqlite - файл создастся  

## Описание запуска проекта

1. Клонируйте проект в папку:

```bash
git clone https://github.com/YaroslavIonin/medical_api.git

```

2. Создайте виртуальное окружение:

```bash
python -m venv venv

```

3. Активируйте виртуальное окружение:

```bash
source venv/bin/activate

```

4. Установите все зависимости из requirements.txt:

```bash
pip install -r requirements.txt

```

5. Выполните миграции:

```bash
python server/manage.py migrate

```

6. Запустите проект:

```bash
python server/manage.py runserver

```

7. Swagger документация http://127.0.0.1:8000/swagger/