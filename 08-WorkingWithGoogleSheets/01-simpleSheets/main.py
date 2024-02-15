import pandas
url = 'https://docs.google.com/spreadsheets/d/1OS3sMy3jUDED4f-7J4n8vr8CBLK3jyKlLWJxTTmu-sI/tq?tqx=out:csv&sheet=2013'
data = pandas.read_csv(url)