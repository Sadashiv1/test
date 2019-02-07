import urllib
import requests
import csv
import json
import urllib3
from pandas import DataFrame
from urllib.request import urlretrieve

token = 'EAAEJotUciGgBAL1XvV9uwGuKImmPcfRhMZAawy0CZCC4MGzUMqZCbwEZBZARLxKnV5R60I5Ffms57XIZBnbsmozp7arnu0sPby4SOAO4RgdErXrqcl34A04PBwW60zlu5mE5c5ZC0Fu1DAaTBn4tPbqZAGJDWpWGmYWdaZC0oNQDXC9fZA6POpzLVdo4AQJ9TaegTx5ImucMfrQwZDZD'
class FbData:
    global token

    def get_info(self):                             # To get info of the user
        me='https://graph.facebook.com/v3.2/me?fields=id,name&access_token=' + token
        me1=requests.get(me)
        print(me1.text)

    def get_photos(self):                           # To get photos into the .csv file
        photos = 'https://graph.facebook.com/v3.2/me?fields=id,name,photos{picture,link}&access_token=' + token
        s1=requests.get(photos)
        s1=s1.json()
        df =DataFrame(s1['photos']['data'])
        export_csv=df.to_csv("/home/nineleaps/PycharmProjects/PythonProgs/ExtractData/Names.csv")


    def get_download_links(self):                     # Funtion to Download photos

        with open('Names.csv', 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            your_list.pop(0)                        # To remove the first element of list as it is of no  use
            l=len(your_list)

        for i,j in enumerate(your_list):        # traversing the list to find the links of photos
            print(j[-1])
            self.download(j[-1], i)

    def download(self,url,dest_path):               # function to download the photos by traversing the each links
                                                    # present in the list
        urlretrieve(url, "Image{}".format(dest_path)+".jpg")        #retrieving the photo from the link availabe and
                                                                    #storing them into the destination path with files
                                                                    #names as Image{1,2,3,4,5,6,7,8........}

f1  =  FbData()                                     #creating object of the FbData Class
f1.get_info()




f1.get_photos()
f1.get_download_links()                              #calling the GetdownloadLink_methods to get the link.


