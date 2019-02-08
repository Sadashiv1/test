import requests
import csv
import json
from pandas import DataFrame


token = 'EAAfUBOZAZAuLABALXV8jxHdLggifyfyxvFse6gXtOBJQOeJTRnC54UxjcqwwzZBoBR9fnQ0e3M8mZAYF8gYtftKUkXQ4jljTywpf0HqPt4XErqRw4gy8Pn8PhubxZBB7ElOLZAvzAuNHOeYSoNjxDvQpdwJTpuZCZCdeGZBwoZBqXJrZBXGTDRiiEUbsxwZBJc2npQiEIfaYsYnGVZAHyHFjwZCPATnU1F5iCe2wgZD'

class FaceBk:
    global token



    def user_inf(self):
        me = 'https://graph.facebook.com/v3.2/me?fields=id,name,albums{photos.limit(10){link}}&access_token=' + token
        n1 = requests.get(me)
        n1.text

    def friend_info(self):
        friends = 'https://graph.facebook.com/v3.2/me?fields=id,name,albums{photos.limit(10){link}}&access_token=' + token
        f1 = requests.get(friends)
        f1.text

    def photos_f(self):
        photo = 'https://graph.facebook.com/me?fields=albums{photos{picture}}&access_token=' + token
        p1 = requests.get(photo)
        p1=p1.json()
        print (p1)
        l = (len(p1['albums']['data'][0]['photos']['data'][0]['picture']))
        f = open("pa.txt", "w")
 #       for i in range(l):

 #           p = (p1['albums']['data'][0]['photos']['data'][0]['picture'])
 #          f.write("\n"+p)

        df= DataFrame(p1['albums']['data'][0]['photos']['data'])
        ex = df.to_csv(("/home/nineleaps/PycharmProjects/parvathi_pro/par.csv"))


        # for i in range(l):
        #     f.write("\n"+p1['albums']['data'][0]['photos']['data'][i]['link'])
        # f.close()

i = FaceBk()
i.photos_f()
