import re

def process_text(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

            first_sentence = re.split(r'(?<=[.!?])', text)[0]

            words = re.findall(r'\w+', first_sentence.lower())

            ukrainian_words = sorted([word for word in words if re.match(r'^[а-яїієґ]+$', word)])
            english_words = sorted([word for word in words if re.match(r'^[a-z]+$', word)])

            word_count = len(words)

            print("Перше речення:")
            print(first_sentence)
            print("\nУкраїнські слова (в алфавітному порядку):")
            print(ukrainian_words)
            print("\nАнглійські слова (в алфавітному порядку):")
            print(english_words)
            print("\nЗагальна кількість слів: {}".format(word_count))

    except FileNotFoundError:
        print("Помилка: Файл не знайдено")
    except Exception as e:
        print("Помилка: {}".format(str(e)))

process_text('text.txt')