"""Chat Bot AI

Original file is located at
    https://colab.research.google.com/drive/1nipqT5xf6dLm_k6J3Arl1-Jrni5U2qF2
"""

import random
import pyjson5
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

config_file_path = "BOT_CONFIG.json"
BOT_CONFIG = {"intents" : {}}
with open(config_file_path, 'r', encoding='UTF-8') as f:
  BOT_CONFIG = pyjson5.load(f)
  # Cleaning empty intents
  #for intent in BOT_CONFIG0['intents'].keys():
   # if BOT_CONFIG0['intents'][intent]['examples'][0] != '':
   #   BOT_CONFIG['intents'] = { intent : {'examples' : BOT_CONFIG0['intents'][intent]['examples'][:]}}
   #   BOT_CONFIG['intents'][intent] = {'responses' : BOT_CONFIG0['intents'][intent]['responses'][:]}
#print(BOT_CONFIG)

intents = []
texts = []
for intent in BOT_CONFIG['intents'].keys():
  for word in BOT_CONFIG['intents'][intent]['examples']:
    intents.append(intent)
    texts.append(word)
len(texts), len(intents)
# intents являются классами признаков, представляют собой строки

#print(texts)
#print(intents)

train_texts, test_texts, intents_train, intents_test = train_test_split(texts, intents, test_size=0.2, random_state=90)
#print(train_texts)
#print(test_texts)
#print(intents_train)
#print(intents_test)

def clean_text(text):
  result = ""
  for letter in text:
    letter = letter.lower()
    if letter in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя ":
      result += letter
  return result

# ngram_range={1,5}, analyzer='char_wb' preprocessor=clean_text
vectorizer = CountVectorizer(encoding='utf-8', lowercase=True,
  ngram_range=(1,1), analyzer='word', preprocessor=clean_text) 
X_train = vectorizer.fit_transform(train_texts)
X_test = vectorizer.transform(test_texts)


vocab = vectorizer.get_feature_names_out()
print(vocab)
#len(vocab)

#clf = LogisticRegression(solver='saga', penalty='elasticnet', l1_ratio=0)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, intents_train)

print("Общий результат:", clf.score(X_train, intents_train),
      "Результат на мин. тестах:", clf.score(X_test, intents_test))

#clf.predict(vectorizer.transform(['здорово']))
#clf.predict(vectorizer.transform(['пока']))


def get_intent_by_model(text):
   return clf.predict(vectorizer.transform([text]))[0]

def chat_bot(input_text):
  intent = get_intent_by_model(input_text)
  return random.choice(BOT_CONFIG['intents'][intent]['responses'])

user_text = ''
while user_text != "стоп":
    user_text = input()
    if user_text != "стоп":
      response = chat_bot(user_text)
      print(response)
