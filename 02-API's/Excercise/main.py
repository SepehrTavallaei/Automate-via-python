import requests
from datetime import datetime
import time
# "api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}"
def api_maker():
    api_key = '21cd575b890a143477ce8e0465cda09d'
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q=Tehran,IR&mode=json&appid={api_key}")
    content = response.json()
    return content


def main():
    data = api_maker()
    for dt in data['list']:
        with open("data.txt",'a') as page:
            page.write(f'London,{time.ctime(dt['dt'])},{dt['weather'][0]["description"]}\n')
            
    
main()
