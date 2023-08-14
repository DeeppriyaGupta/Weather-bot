import win32com.client as wc
import requests
import json

city=input('city: ')
url=f'https://api.weatherapi.com/v1/current.json?key=b8f6078273c04b76990190942231108&q={city}'
r=requests.get(url)

temp=json.loads(r.text)['current']['temp_c']
country=json.loads(r.text)['location']['country']
humidity=json.loads(r.text)['current']['humidity']
speak= wc.Dispatch('SAPI.SpVoice')
i=f'the weather of the {city} in {country} is {temp} and the humidity is {humidity}'
print(f'the weather of the {city} in {country} is {temp} and the humidity is {humidity}')
speak.Speak(i)