from datetime import datetime

from django.shortcuts import redirect, render
from django.urls import reverse

from .data import COUNTRIES, TRANSPORT_CHOICES, TRANSLATIONS
from .forms import SettingsForm, TripForm


def _get_context(request):
    lang = request.COOKIES.get("lang", "ru")
    if lang not in TRANSLATIONS:
        lang = "ru"

    theme = request.COOKIES.get("theme", "light")
    if theme not in ("light", "dark"):
        theme = "light"

    last_visit = request.COOKIES.get("last_visit", "")
    previous_visit = request.COOKIES.get("previous_visit", "")
    visits = int(request.COOKIES.get("visits", 0))

    trips = request.session.get("trips", [])

    return {
        "t": TRANSLATIONS[lang],
        "lang": lang,
        "theme": theme,
        "last_visit": last_visit,
        "previous_visit": previous_visit,
        "visits": visits,
        "trips": trips,
        "trips_count": len(trips),
        "current_year": datetime.now().year,
    }


def _update_visit_cookies(request, response):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    prev = request.COOKIES.get("last_visit", "")
    visits = int(request.COOKIES.get("visits", 0)) + 1

    if prev:
        response.set_cookie("previous_visit", prev, max_age=60 * 60 * 24 * 365)
    response.set_cookie("last_visit", now, max_age=60 * 60 * 24 * 365)
    response.set_cookie("visits", visits, max_age=60 * 60 * 24 * 365)


def _country_label(code, lang):
    for c in COUNTRIES:
        if c["code"] == code:
            return c["name_en"] if lang == "en" else c["name"]
    return code


def _transport_label(code, lang):
    labels_ru = dict(TRANSPORT_CHOICES)
    labels_en = {"plane": "Plane", "train": "Train",
                 "car": "Car", "bus": "Bus"}
    return labels_en.get(code, code) if lang == "en" else labels_ru.get(code, code)


def index(request):
    ctx = _get_context(request)

    form = TripForm(lang=ctx["lang"])
    settings_form = SettingsForm(
        initial={"theme": ctx["theme"], "language": ctx["lang"]},
    )

    if request.method == "POST":
        if "trip_submit" in request.POST:
            form = TripForm(request.POST, lang=ctx["lang"])
            if form.is_valid():
                trips = request.session.get("trips", [])
                trip = {
                    "id": len(trips) + 1,
                    "name": form.cleaned_data["name"],
                    "country_code": form.cleaned_data["country"],
                    "country": _country_label(
                        form.cleaned_data["country"], ctx["lang"]
                    ),
                    "date": form.cleaned_data["date"].strftime("%d.%m.%Y"),
                    "days": form.cleaned_data["days"],
                    "transport_code": form.cleaned_data["transport"],
                    "transport": _transport_label(
                        form.cleaned_data["transport"], ctx["lang"]
                    ),
                    "budget": form.cleaned_data["budget"] or 0,
                    "notes": form.cleaned_data["notes"],
                    "created": datetime.now().strftime("%d.%m.%Y %H:%M"),
                }
                trips.append(trip)
                request.session["trips"] = trips
                request.session.modified = True
                return redirect(f"{reverse('index')}#trips")

        elif "settings_submit" in request.POST:
            sform = SettingsForm(request.POST)
            if sform.is_valid():
                response = redirect("index")
                response.set_cookie(
                    "theme", sform.cleaned_data["theme"],
                    max_age=60 * 60 * 24 * 365,
                )
                response.set_cookie(
                    "lang", sform.cleaned_data["language"],
                    max_age=60 * 60 * 24 * 365,
                )
                return response

    ctx["form"] = form
    ctx["settings_form"] = settings_form
    ctx["countries"] = COUNTRIES
    ctx["transport_choices"] = TRANSPORT_CHOICES

    response = render(request, "planner/index.html", ctx)
    _update_visit_cookies(request, response)
    return response


def delete_trip(request, trip_id):
    if request.method == "POST":
        trips = request.session.get("trips", [])
        trips = [t for t in trips if t["id"] != trip_id]
        request.session["trips"] = trips
        request.session.modified = True
    return redirect(f"{reverse('index')}#trips")


def clear_trips(request):
    if request.method == "POST":
        request.session["trips"] = []
        request.session.modified = True
    return redirect(f"{reverse('index')}#trips")
