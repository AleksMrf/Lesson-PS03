import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка при получении слова: {e}")

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        try:
            translated_word = GoogleTranslator(source='en', target='ru').translate(word)
            translated_definition = GoogleTranslator(source='en', target='ru').translate(word_definition)
        except Exception as e:
            print(f"Ошибка при переводе: {e}")
            continue

        print(f"Значение слова - {translated_definition}")
        user = input("Что это за слово? ")
        if user.lower() == translated_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {translated_word}")

        play_again = input("Хотите сыграть еще раз? y/n: ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break
word_game()