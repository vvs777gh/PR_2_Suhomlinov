from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .data import COUNTRIES, TRANSPORT_CHOICES, TRANSLATIONS
from .forms import SettingsForm, TripForm


def _get_context(request):
    """Формирует базовый контекст из cookies."""
    lang = request.COOKIES.get("lang", "ru")
    if lang not in TRANSLATIONS:
        lang = "ru"

    theme = request.COOKIES.get("theme", "light")
    if theme not in ("light", "dark"):
        theme = "light"

    last_visit = request.COOKIES.get("last_visit", "")
    previous_visit = request.COOKIES.get("previous_visit", "")
    visits = int(request.COOKIES.get("visits", 0))

    return {
        "t": TRANSLATIONS[lang],
        "lang": lang,
        "theme": theme,
        "last_visit": last_visit,
        "previous_visit": previous_visit,
        "visits": visits,
        "current_year": datetime.now().year,
    }


def _update_visit_cookies(request, response):
    """Обновляет cookie последнего визита и счётчик посещений."""
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    prev = request.COOKIES.get("last_visit", "")
    visits = int(request.COOKIES.get("visits", 0)) + 1

    if prev:
        response.set_cookie(
            "previous_visit", prev, max_age=60 * 60 * 24 * 365
        )
    response.set_cookie("last_visit", now, max_age=60 * 60 * 24 * 365)
    response.set_cookie("visits", visits, max_age=60 * 60 * 24 * 365)


def index(request):
    ctx = _get_context(request)
    ctx.update(
        {
            "form": TripForm(),
            "settings_form": SettingsForm(
                initial={"theme": ctx["theme"], "language": ctx["lang"]}
            ),
            "countries": COUNTRIES,
            "transport_choices": TRANSPORT_CHOICES,
        }
    )

    if request.method == "POST":
        # Обработка формы путешествия
        if "trip_submit" in request.POST:
            form = TripForm(request.POST)
            if form.is_valid():
                ctx["form"] = TripForm()
                ctx["saved_trip"] = form.cleaned_data
                response = render(request, "planner/index.html", ctx)
                _update_visit_cookies(request, response)
                return response
            ctx["form"] = form

        # Обработка формы настроек
        elif "settings_submit" in request.POST:
            sform = SettingsForm(request.POST)
            if sform.is_valid():
                response = redirect("index")
                response.set_cookie(
                    "theme",
                    sform.cleaned_data["theme"],
                    max_age=60 * 60 * 24 * 365,
                )
                response.set_cookie(
                    "lang",
                    sform.cleaned_data["language"],
                    max_age=60 * 60 * 24 * 365,
                )
                return response
            ctx["settings_form"] = sform

    response = render(request, "planner/index.html", ctx)
    _update_visit_cookies(request, response)
    return response
