import requests

urls = [
    "http://google.com/",
    "http://yandex.ru",
    "http://mail.ru",
    "http://vk.com"
    ]

for url in urls:
    for i in range (10):
        response = requests.get (url)
        status = response.status_code
        print (f"Запрос № {i + 1} сайта {url}. Статус-код {status}.")
