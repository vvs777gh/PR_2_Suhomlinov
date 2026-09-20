# Travel Planner (Планировщик путешествий)

Django-проект для планирования путешествий с сохранением пользовательских
настроек (тема, язык, последний визит) в cookies.

## Функционал

- Форма планирования поездки: имя, страна, дата, длительность, транспорт,
  бюджет, заметки
- Переключение темы (светлая / тёмная) и языка (RU / EN) через cookies
- Сохранение даты последнего визита и счётчика посещений
- Карточки популярных направлений с изображениями
- Адаптивный дизайн
- Тесты (`planner/tests.py`)

## Установка

```bash
git clone <repo-url>
cd travel_planner

python -m venv venv

# Windows (CMD)
venv\Scripts\activate
# Windows (PowerShell) — при ошибке выполните один раз:
#   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Открыть в браузере: http://127.0.0.1:8000/

## Тесты

```bash
python manage.py test
```

## Структура

```
travel_planner/
├── config/                 # настройки проекта
├── planner/                # приложение
│   ├── data.py             # данные (страны, переводы)
│   ├── forms.py            # формы
│   ├── views.py            # представления
│   └── tests.py            # тесты
├── templates/planner/      # шаблоны
├── static/css/             # стили
├── static/images/          # изображения
├── requirements.txt
└── README.md
```
