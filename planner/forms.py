from django import forms

from .data import COUNTRIES, TRANSPORT_CHOICES, THEMES, LANGUAGES


class TripForm(forms.Form):
    def __init__(self, *args, lang="ru", **kwargs):
        super().__init__(*args, **kwargs)
        self.lang = lang

        labels = {
            "ru": {
                "name": "Ваше имя",
                "country": "Страна",
                "date": "Дата поездки",
                "days": "Количество дней",
                "transport": "Транспорт",
                "budget": "Бюджет, ₽",
                "notes": "Заметки",
            },
            "en": {
                "name": "Your name",
                "country": "Country",
                "date": "Travel date",
                "days": "Number of days",
                "transport": "Transport",
                "budget": "Budget, ₽",
                "notes": "Notes",
            },
        }
        L = labels.get(lang, labels["ru"])

        self.fields["name"].label = L["name"]
        self.fields["country"].label = L["country"]
        self.fields["date"].label = L["date"]
        self.fields["days"].label = L["days"]
        self.fields["transport"].label = L["transport"]
        self.fields["budget"].label = L["budget"]
        self.fields["notes"].label = L["notes"]

        # Локализуем варианты в select
        if lang == "en":
            self.fields["country"].choices = [
                (c["code"], c["name_en"]) for c in COUNTRIES
            ]
            self.fields["transport"].choices = [
                ("plane", "Plane"),
                ("train", "Train"),
                ("car", "Car"),
                ("bus", "Bus"),
            ]
        else:
            self.fields["country"].choices = [
                (c["code"], c["name"]) for c in COUNTRIES
            ]
            self.fields["transport"].choices = TRANSPORT_CHOICES

        # Placeholder
        placeholders = {
            "ru": "Иван Иванов",
            "en": "John Smith",
        }
        self.fields["name"].widget.attrs["placeholder"] = placeholders.get(
            lang, "")

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(),
    )
    country = forms.ChoiceField(choices=[])
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    days = forms.IntegerField(min_value=1, max_value=90, initial=7)
    transport = forms.ChoiceField(choices=[])
    budget = forms.IntegerField(
        min_value=0, required=False,
        widget=forms.NumberInput(attrs={"placeholder": "50000"}),
    )
    notes = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        required=False,
    )


class SettingsForm(forms.Form):
    theme = forms.ChoiceField(choices=THEMES, label="Тема / Theme")
    language = forms.ChoiceField(choices=LANGUAGES, label="Язык / Language")
