import requests
import json
import sqlite3
import datetime

months= {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,\
    'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,\
    'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}

url='https://hubofdata.ru/storage/f/2013-08-18T19%3A58%3A51.196Z/greetings-data.json'
response=requests.get(url)


conn=sqlite3.connect('db.sqlite3')
cursor=conn.cursor()

for i in response.json().get('items'):
    category=i['category']
    from_name=i['from']
    title = i['title']
    text = i['text']
    thedate = datetime.date(int(i['thedate'].split(' ')[2]), int(months.get(i['thedate'].split(' ')[1])), int(i['thedate'].split(' ')[0]))
    id=i['id']
    if "'" in text:
        index=text.index("'")
        text=text[:index] + text[index+1:]
    cursor.execute(f'''INSERT INTO api_items (category, from_items, title, text, thedate, id_items)\
    VALUES ('{category}', '{from_name}', '{title}', '{text}', '{thedate}', {id})''')
    conn.commit()

cursor.close()
conn.close()