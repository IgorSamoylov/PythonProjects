"""
Ученые нашли табличку с текстом на языке племени Мумба-Юмба.
Определите, сколько уникальных слов содержится в этом тексте.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Большие и маленькие буквы считаются различными.

В этой и последующих задачах этого занятия вам нужно скачать файл по ссылке,
запустить свой скрипт на собственном компьютере и ввести только ответ конкретно
для этого файла.
"""

inp_file = open("TEST_TEXT.txt", "r", encoding="UTF-8")

uniq_words = set()
for line in inp_file:     # По умолчанию файловый объект итерируется по строкам!
    uniq_words.update(line.split()) # Метод update сета позволяет обновить его списком!

print(len(uniq_words))
