meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "ТИП-ТОП": "Когда всё хорошо",
            "ЧИЛ": "Время отдыха",
            "ДЕД-ИНСАЙД": "Культура грусти у подростков"
            }
word = input("Введите непонятное слово (большими буквами!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Такого слова нету в словаре")
