# the most common type of API are rest API's
# APi are a way that two Application to communicate
# the most usuall format that is served via Api's is json

import requests

# url = ('https://newsapi.org/v2/everything?'
#        'q=Apple&'
#        'from=2024-01-07&'
#        'sortBy=popularity&'
#        'apiKey=dc7edd70ff6f4577a966cdf0406381d0')

# response = requests.get(url)
# content = response.json()
def get_news(topic,from_date,api_key='dc7edd70ff6f4577a966cdf0406381d0'):
    url = f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&sortBy=popularity&apiKey=dc7edd70ff6f4577a966cdf0406381d0"
    r = requests.get(url)
    content = r.json()
    print(content)



get_news('Love','2024-01-07','dc7edd70ff6f4577a966cdf0406381d0')