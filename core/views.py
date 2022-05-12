from django.shortcuts import render
import json
from random import randint

def get_words():
    
    with open("core/data/nouns.json", "r") as file:
        data = json.load(file)

    word_index = randint(0, 100)

    word = {
        "ita_word":data["nouns"][word_index]["ita"],
        "eng_word":data["nouns"][word_index]["eng"]
    }
    
    return word


def index(request):
    context = {
        "word":get_words()
    }

    return render(request, "index.html", context)
