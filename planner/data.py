COUNTRIES = [
    {
        "code": "tr",
        "name": "Турция",
        "name_en": "Turkey",
        "description": "Страна на стыке Европы и Азии. Идеальна для пляжного отдыха.",
        "image": "images/turkey.jpg",
        "price": 45000,
    },
    {
        "code": "it",
        "name": "Италия",
        "name_en": "Italy",
        "description": "Колыбель Ренессанса, римские руины и лучшая паста.",
        "image": "images/italy.jpg",
        "price": 78000,
    },
    {
        "code": "jp",
        "name": "Япония",
        "name_en": "Japan",
        "description": "Страна восходящего солнца: сакура, технологии и традиции.",
        "image": "images/japan.jpg",
        "price": 120000,
    },
    {
        "code": "eg",
        "name": "Египет",
        "name_en": "Egypt",
        "description": "Пирамиды, Красное море и древняя история.",
        "image": "images/egypt.jpg",
        "price": 55000,
    },
]

TRANSPORT_CHOICES = [
    ("plane", "Самолёт"),
    ("train", "Поезд"),
    ("car", "Автомобиль"),
    ("bus", "Автобус"),
]

LANGUAGES = [
    ("ru", "Русский"),
    ("en", "English"),
]

THEMES = [
    ("light", "Светлая"),
    ("dark", "Тёмная"),
]

TRANSLATIONS = {
    "ru": {
        "title": "Планировщик путешествий",
        "subtitle": "Спланируйте свою идеальную поездку",
        "form_title": "Новое путешествие",
        "name_label": "Ваше имя",
        "country_label": "Страна",
        "date_label": "Дата поездки",
        "days_label": "Количество дней",
        "transport_label": "Транспорт",
        "budget_label": "Бюджет, ₽",
        "notes_label": "Заметки",
        "save_btn": "Сохранить",
        "settings_title": "Настройки",
        "theme_label": "Тема",
        "language_label": "Язык",
        "save_settings": "Применить",
        "last_visit": "Последний визит",
        "countries_title": "Популярные направления",
        "success": "Путешествие сохранено!",
        "from_price": "от",
    },
    "en": {
        "title": "Travel Planner",
        "subtitle": "Plan your perfect trip",
        "form_title": "New Trip",
        "name_label": "Your name",
        "country_label": "Country",
        "date_label": "Travel date",
        "days_label": "Number of days",
        "transport_label": "Transport",
        "budget_label": "Budget, ₽",
        "notes_label": "Notes",
        "save_btn": "Save",
        "settings_title": "Settings",
        "theme_label": "Theme",
        "language_label": "Language",
        "save_settings": "Apply",
        "last_visit": "Last visit",
        "countries_title": "Popular destinations",
        "success": "Trip saved!",
        "from_price": "from",
    },
}
