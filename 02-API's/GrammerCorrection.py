import requests

def get_api(text):
    url = 'https://api.languagetool.org/v2/check'
    data = {
        'text': text,
        'language': 'auto'
    }
    response = requests.post(url,data)
    content = response.json()
    return content


def main():
    text = input("Enter a text so I can correct you gramatically: ")
    print(get_api(text))

main()
