from django.shortcuts import render
import json
from random import randint

def get_words():
    
    with open("core/data/ita_words.json", "r") as file:
        data = json.load(file)

    word_count = len(data["words"]) # Count how many words there are in ita_words.json

    word_index = randint(0, word_count)

    word = {
        "ita_word":data["words"][word_index]["ita"],
        "eng_word":data["words"][word_index]["eng"]
    }
    
    return word


def index(request):
    context = {
        "word":get_words()
    }

    return render(request, "index.html", context)
