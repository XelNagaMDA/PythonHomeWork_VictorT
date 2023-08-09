"""
Create an application that will translate text.

Application should prompt the user for the target language from a list of options. (You decide what the options are)

Application should allow user to input any length text, or can provide a path to a file (textual file to translate)

Write the code as a library, this way you can have functions such as:

    get_all_languages
    translate(text, to_language)
    translate_file(path, to_language)

"""
import requests


def get_all_languages():
    languages = ["en", "it", "de", "ro", "es", "fr"]
    source_choice = input("Please choose the source language: ")
    to_translate = input("Please choose the language to translate to: ")
    if source_choice not in languages:
        raise Exception("Invalid source language")

    if to_translate not in languages:
        raise Exception("Invalid target language")

    return source_choice, to_translate


def file_to_translate():
    with open('traducere.txt', 'r') as file:
        content = file.read()
        return content


def api_key():
    with open('api_key.txt', 'r') as file:
        content = file.read()
        return content


def translation(source_choice, to_translate):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "source": source_choice,
        "target": to_translate,
        "q": file_to_translate()
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": api_key(),
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.json())


source_choice, to_translate = get_all_languages()
translation(source_choice, to_translate)
