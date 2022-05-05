from django.shortcuts import render


def get_words():
    ita_word = "Ciao"
    eng_word = "Hello"

    word = {
        "ita_word":ita_word,
        "eng_word":eng_word
    }

    return word


def index(request):
    context = {
        "word":get_words()
    }

    return render(request, "index.html", context)
