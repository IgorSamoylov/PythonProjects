import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
"class %%%(%%%) : " :
"Создается класс с именем %%%, наследующим %%%.",

"class %%%(object):\n\tdef init (self, ***)" :
"Класс %%% комбинирует __init_ с параметрами self и параметрами ***." ,

"class %%%(object):\n\tdef *** (self, @0@)" :
"Класс %%% комбинирует функцию с именем *** с параметрами self и @@@." ,

"*** = %%%()":
"Создается *** как экземпляр класса %%%." ,

"***_***(@@@)" :
"Из *** получается функция ***, а затем вызывается с параметрами self, @@@.",

"***.*** = '***'" :
"Из *** получается атрибут ***, а затем устанавливается равным '***'."
}

# тренировка запоминания фраз
if len(sys.argv) == 2 and sys.argv[l] == "russian" :
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# подгружаем слова с сервера
for word in urlopen(WORD_URL).readlines() :
    WORDS.append(str(word.strip(), encoding="utf-8 "))

def convert (snippet, phrase) :
    class_names = [w.capitalize() for w in
                            random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")) :
        param_count = random.randint(1,3)
        param_names.append(', '.join(
        random.sample(WORDS, param_count)))

    for sentence in snippet, phrase : 
        result = sentence [:]

        # вымышленные имена классов
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # вымышленные прочие имена
        for word in other_names:
            result = result.replace("***", word, 1)

        # с п и с о к в ы м ы ш л е н н ы х п а р а м е т р о в
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# выполнение, пока не нажато сочетание клавиш CTRL+Z
try:
    while True:
        snippets = list (PHRASES.keys ())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert (snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ОТВЕТ: {answer}\n\n")
except EOFError:
    print("\nПока")

