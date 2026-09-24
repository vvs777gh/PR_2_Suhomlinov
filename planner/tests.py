def test_trip_saved_to_session(self):
    """Валидная форма сохраняет поездку в сессию и делает redirect."""
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
    self.assertEqual(response.status_code, 302)

    session = self.client.session
    trips = session.get("trips", [])
    self.assertEqual(len(trips), 1)
    self.assertEqual(trips[0]["name"], "Иван")
    self.assertEqual(trips[0]["country"], "Италия")

    # Поездка видна на странице
    response = self.client.get(reverse("index"))
    self.assertContains(response, "Иван")
    self.assertContains(response, "Италия")


def test_trip_english_labels(self):
    """При lang=en лейблы формы и стран на английском."""
    self.client.cookies["lang"] = "en"
    response = self.client.get(reverse("index"))
    html = response.content.decode("utf-8")
    self.assertIn("Your name", html)
    self.assertIn("Travel date", html)
    self.assertIn("Italy", html)
    self.assertNotIn("Ваше имя", html)


def test_clear_trips(self):
    """Очистка всех поездок удаляет их из сессии."""
    session = self.client.session
    session["trips"] = [{"id": 1, "name": "Test"}]
    session.save()

    response = self.client.post(reverse("clear_trips"))
    self.assertEqual(response.status_code, 302)
    self.assertEqual(self.client.session.get("trips"), [])
