import urllib
import requests
import csv
import json
import urllib3
from pandas import DataFrame
from urllib.request import urlretrieve

token = 'EAAEJotUciGgBAGfZB8koZCyeFY76jtuwb4Ib9gK5P90FiwnExUxKqH3a9EkohVpR2n9tS5Wiyi3ZBEKZBcpVr4NM6BsI7ZCDhSZCE1aETCEJAVFPVMTZBjMiqjl2TniZCaVU1yOclg8EkMscceXGqgm1ZB2dBAy7LkQNstj9CCW8ZAPRZCSlZA55iLrFWhddE6SPCUjzokjVzt0jgAZDZD'
class FbData:
    global token

    def get_photos(self):
        photos = 'https://graph.facebook.com/v3.2/me?fields=id,name,photos{picture,link}&access_token=' + token
        s1=requests.get(photos)
        s1=s1.json()
        df =DataFrame(s1['photos']['data'])
        export_csv=df.to_csv("/home/nineleaps/PycharmProjects/PythonProgs/ExtractData/Names.csv")


#        urllib.urlretrieve("", "00000001.jpg")

    def download_photos(self):

        with open('Names.csv', 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            your_list.pop(0)
            l=len(your_list)

            for i,j in enumerate(your_list):
                print(j[-1])
                self.download(j[-1], i)


    def download(self, url, dest_path):
        urlretrieve(url, "Image{}".format(dest_path)+".jpg")

f1 = FbData()
f1.download_photos()



