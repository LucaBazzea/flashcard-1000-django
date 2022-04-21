from django.shortcuts import render


def index(request):
    context = {
        "ita_word":"Ciao",
        "eng_word":"Hello"
    }
    return render(request, "index.html", context)
