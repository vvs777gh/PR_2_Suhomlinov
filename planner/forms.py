from django import forms

from .data import COUNTRIES, TRANSPORT_CHOICES, THEMES, LANGUAGES


class TripForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Ваше имя",
        widget=forms.TextInput(attrs={"placeholder": "Иван Иванов"}),
    )
    country = forms.ChoiceField(
        choices=[(c["code"], c["name"]) for c in COUNTRIES],
        label="Страна",
    )
    date = forms.DateField(
        label="Дата поездки",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    days = forms.IntegerField(
        min_value=1,
        max_value=90,
        initial=7,
        label="Количество дней",
    )
    transport = forms.ChoiceField(
        choices=TRANSPORT_CHOICES,
        label="Транспорт",
    )
    budget = forms.IntegerField(
        min_value=0,
        required=False,
        label="Бюджет, ₽",
        widget=forms.NumberInput(attrs={"placeholder": "50000"}),
    )
    notes = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 3, "placeholder": "Пожелания..."}),
        required=False,
        label="Заметки",
    )


class SettingsForm(forms.Form):
    theme = forms.ChoiceField(choices=THEMES, label="Тема")
    language = forms.ChoiceField(choices=LANGUAGES, label="Язык")
