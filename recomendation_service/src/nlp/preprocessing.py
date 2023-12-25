import re

import pymorphy3
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")

morph = pymorphy3.MorphAnalyzer()


def get_normal_form_word(word):
    return morph.parse(word)[0].normal_form


def del_useless_signs(phrase):
    return re.sub("[^а-яa-z0-9'№ -]", "", phrase)


def get_normal_form_phrase(phrase):
    wordArr = word_tokenize(phrase, language="russian")
    return " ".join(get_normal_form_word(word) for word in wordArr)


def toLower(phrase):
    return phrase.lower()


def preprocessing(phrase):
    phrase = toLower(phrase)
    phrase = del_useless_signs(phrase)
    return get_normal_form_phrase(phrase)
