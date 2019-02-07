import urllib
import requests
import csv
import json
import urllib3
from pandas import DataFrame
from urllib.request import urlretrieve

token='EAAEFCck16fEBADP7xUYixZCpWAEjbMjE0ap8vK7FZBSOiosZAY4Dso3OA3d0ktPHvZBEcfwihuyiRj9UFNkRXOUdA5hSDRqrfPRStiW2ePxf7ZBZAZBjqZCX1W3v6zkJ2JxxIWy1mdBAb0tOZAl7j1xxNtRUxxZAc9ZAHpVHH2mcEk9Gnk4BmbwZBDrahCwGz5qCbnbOWi3V1lDVJAZDZD'


class Ishita:
    global token

    def user_info(self):
        me = 'https://graph.facebook.com/v3.2/me?fields=id,name,photos.limit(10){picture,link}&access_token=' + token
        me1 = requests.get(me)
        print(me1.text)

    def user_friends(self):
        friends = 'https://graph.facebook.com/v3.2/me?fields=id,name,photos.limit(10){picture,link}&access_token=' + token
        f1 = requests.get(friends)
        print(f1.text)

    def GetPhotos(self):

        photo = 'https://graph.facebook.com/me?fields=id,name,photos.limit(10){picture,link}&access_token=' + token
        p1 = requests.get(photo)
        p1 = p1.json()
        print(p1)
        df = DataFrame(p1['photos']['data'])
        export_csv = df.to_csv("/home/nineleaps/PycharmProjects/ishu/venv/is.csv")

    def GetDownloadLinks(self):

        with open('is.csv', 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            your_list.pop(0)                         # To remove the first element of list as it is of no  use
            l = len(your_list)
        for i, j in enumerate(your_list):        # traversing the list to find the links of photos
            print(j[-1])
            self.Download(j[-1], i)

    def Download(self, url, dest_path):       # function to download the photos by traversing the each links
                # present in the list
        urlretrieve(url,"Image{}".format(dest_path) + ".jpg")       # retrieving the photo from the link availabel and
                                                                            #  storing them into the destination path with files
                                                                            #  names as Image{1,2,3,4,5,6,7,8........}


i1 = Ishita()                              # creating object of the FbData Class
i1.user_info()
i1.GetPhotos()
i1.GetDownloadLinks()                      # calling the GetdownloadLink_methods to get the link.

