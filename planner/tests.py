from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):

    def test_index_status_code(self):
        """Главная страница открывается."""
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_sets_visit_cookies(self):
        """При заходе ставятся cookies last_visit и visits."""
        response = self.client.get(reverse("index"))
        self.assertIn("last_visit", response.cookies)
        self.assertIn("visits", response.cookies)

    def test_theme_cookie_saved(self):
        """Настройки темы и языка сохраняются в cookies."""
        response = self.client.post(
            reverse("index"),
            {"theme": "dark", "language": "en", "settings_submit": ""},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.cookies["theme"].value, "dark")
        self.assertEqual(response.cookies["lang"].value, "en")

    def test_index_dark_theme_applied(self):
        """Cookie theme=dark добавляет класс theme-dark."""
        self.client.cookies["theme"] = "dark"
        response = self.client.get(reverse("index"))
        self.assertContains(response, "theme-dark")

    def test_index_english_lang(self):
        """Cookie lang=en переключает интерфейс на английский."""
        self.client.cookies["lang"] = "en"
        response = self.client.get(reverse("index"))
        self.assertContains(response, "Travel Planner")

    def test_trip_form_valid_submit(self):
        """Валидная форма путешествия возвращает сообщение об успехе."""
        response = self.client.post(
            reverse("index"),
            {
                "name": "Иван",
                "country": "it",
                "date": "2025-07-01",
                "days": 10,
                "transport": "plane",
                "budget": 80000,
                "notes": "Хочу в Рим",
                "trip_submit": "",
            },
        )
        self.assertContains(response, "Иван")

    def test_trip_form_invalid(self):
        """Форма с пустым именем не проходит валидацию."""
        response = self.client.post(
            reverse("index"),
            {
                "name": "",
                "country": "it",
                "date": "2025-07-01",
                "days": 10,
                "transport": "plane",
                "trip_submit": "",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Обязательное поле")
