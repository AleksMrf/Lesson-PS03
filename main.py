from bs4 import BeautifulSoup
import requests
from googletrans import Translator


def get_english_words():
    url = "https://randomword.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на успешный запрос

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")

        # Получаем слово
        word_element = soup.find("div", id="random_word")
        word_definition_element = soup.find("div", id="random_word_definition")

        # Проверяем, что элементы найдены
        if word_element and word_definition_element:
            english_words = word_element.text.strip()
            word_definition = word_definition_element.text.strip()
            return {
                "english_words": english_words,
                "word_definition": word_definition
            }
        else:
            print("Не удалось найти слово или его определение.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")

    # Инициализация переводчика
    translator = Translator()

    while True:
        # Получаем случайное слово
        word_dict = get_english_words()

        # Проверяем, что word_dict не None
        if word_dict is None:
            print("Попробуйте снова позже.")
            break

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и его определение на русский
        russian_word = translator.translate(word, dest='ru').text
        russian_definition = translator.translate(word_definition, dest='ru').text

        # Начинаем игру
        print(f"Значение слова - {russian_definition}")
        user = input("Что это за слово? ")
        if user.lower() == russian_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {russian_word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n: ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


word_game()