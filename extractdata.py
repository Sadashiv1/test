import requests
import csv

token='EAAEFCck16fEBAMjoDBq5GyQ8RjqvGpqTmY9d7s1d8RhAfrilDefESLaUthrBLR9ah5LNX4ves6hTLpC8vMfuGgZB5NCGG1YS29DTxtUEL4W7c36rD3XxNZAiIPPmWJ52MDZCHozP8R1hQcyaeuSUZAFe76TIecsXg5QQeZAXFW7WAcy6KI9CdMlZByaiYAR78SakSqSxncXwZDZD'

class Ishita():
    global token
    me = 'https://graph.facebook.com/v3.2/me?fields=id,name&access_token=' + token


    friends = 'https://graph.facebook.com/v3.2/me/friends?fields=id,name&access_token=' + token
    photo = 'https://graph.facebook.com/me?fields=id,name,address,photos.limit(10)&access_token=' + token

    me1 = requests.get(me)
    f1 = requests.get(friends)
    p1 = requests.get(photo)

    print(me1.text)
    print(f1.text)
    print(p1.json())
