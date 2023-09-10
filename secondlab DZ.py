import requests

city = "Moscow, RU"
appid = "86dbb11b362e5fc4b1de1200eea9645e"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'], "градусов по Цельсию")
print("Минимальная температура:", data['main']['temp_min'], "градусов по Цельсию")
print("Максимальная температура", data['main']['temp_max'], "градусов по Цельсию")
print("Скорость ветра : ", data['wind']['speed'], "м/с")
print("Видимость : ", data['visibility'], "метров")



res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("ПРОГНОЗ ПОГОДЫ НА НЕДЕЛЮ:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
    '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
    i['weather'][0]['description'], "> \r\nСкорость ветра <", i['wind']['speed'], "м/с", "> \r\nВидимость <", i['visibility'], "метров")
print("____________________________")
