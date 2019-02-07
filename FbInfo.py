import requests
import pandas as pd


'''A simplistic definition of a Graph API is an API that models the data in terms of 
nodes and edges (objects and relationships) and allows the client to interact with 
multiple nodes in a single request.

Typically we use nodes to get data about a specific object, use edges to get 
collections of objects on a single object, and use fields to get data about a single
object or each object in a collection.'''

''' For this code, you have to obtain following data:
    1. Access token id 
    2. Location of CSV File
    3. Location of folder in which you want to store images.'''


token='EAAIml3mqbZAoBABygBeiryjelZBUraJutDMZCAAI5ZAG8EPHxQYEKVZAnTE0GxXq3ZBpJi1rXpklLQXhNTrtk4X0MImiTRu4zxzTmXNe8TfMtTr9Nc8fDFRKFWm0Lh00qIZArZA4wUCPjorEK65z4xJvgfUvJMfZCjy8tMNZAsoZAG8aXs3aX2jJ5iAPaTVTm5V9sJoV15cpkiK9wZDZD'
location_csv_file = '/home/nineleaps/FBPhotos.csv'
location_of_folder = '/home/nineleaps/photos/'

class FbInfo:

  global token  # calling the global variable in the class
  global location_csv_file
  global location_of_folder

  def get_user_name(self):

    nam= "https://graph.facebook.com/v3.2/me?fields=name&access_token="+token
    name = requests.get(nam)  # requesting the data(name) of url.
    namejson = name.json()   # converting file in json format which is readable in python as dictionary.
    print ('Name:',namejson['name'])

  def get_birthday(self):

    dat= "https://graph.facebook.com/v3.2/me?fields=birthday&access_token="+token
    date = requests.get(dat)
    datej = date.json()
    print ('DOB:',datej['birthday'])

  def get_location(self):

    location= "https://graph.facebook.com/v3.2/me?fields=location&access_token="+token
    loc = requests.get(location)
    locationjson = loc.json()
    print ('Location:', locationjson['location']['name'])

  def get_posts(self):
    df = pd.read_csv(location_csv_file)  # creating a dataframe using pandas
    pos= "https://graph.facebook.com/v3.2/me?fields=posts{message}&access_token="+token
    post = requests.get(pos)
    postj = post.json()
    list_of_caption =[]  # intializing an empty list to store the captions
    length_of_json_post_file = len( postj['posts']['data'])  #
    for n in range(length_of_json_post_file):
      if 'message' in ( postj['posts']['data'][n]).keys():  # storing caption if available
        list_of_caption.append(postj['posts']['data'][n]['message'])
      else:  # storing None if unavailable
        list_of_caption.append('None')
    df['List of  Post Captions'] = list_of_caption  # transfering obtained list into dataframe
    df.to_csv(location_csv_file,index=False)  # converting dataframe into .csv file
    print('List of post captions are updated in csv file')

  def get_photos(self):

    df = pd.read_csv(location_csv_file)  # creating a dataframe using pandas
    photolink = "https://graph.facebook.com/v3.2/me?fields=photos.limit(18){link,created_time,picture}&access_token="+token
    photos = requests.get(photolink)
    photoj = photos.json()
    Photo_Link = []
    Created_time= []
    Downloadable_Link = []
    for i in range(len(photoj['photos']['data'])):
      Photo_Link.append((photoj['photos']['data'])[i]['link'])
      Created_time.append((photoj['photos']['data'])[i]['created_time'])
      Downloadable_Link.append((photoj['photos']['data'])[i]['picture'])
    df['List of Photo link']=(Photo_Link)
    df['List of Created Time']=(Created_time)
    df['List of Downloadable link']=(Downloadable_Link)
    df.to_csv(location_csv_file,index=False)  # converting dataframe into .csv file without indices
    print("List of Photo links, created time and downloadable link are updated in csv file")

  def download_pics(self):

    i=0
    df = pd.read_csv(location_csv_file)  # creating a dataframe using pandas
    lists = df['List of Downloadable link']  # obtaining column for list of downloadable using data frame
    for list in lists:
      img_data = requests.get(list).content  #requesting data available in link
      with open((location_of_folder+'fbimage'+ str(i)+".jpg"), 'wb') as downloader:  # opening image file in write(bit) mode
        downloader.write(img_data)  # moving the collected data
      i += 1  # incrementing the variable for changing image name for each link
    print('Download Complete in home/nineleaps/photos folder')


Hars = FbInfo()
Hars.get_user_name()
Hars.get_birthday()
Hars.get_location()
Hars.get_posts()
Hars.get_photos()
Hars.download_pics()
