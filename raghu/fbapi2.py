import requests  # importing the requests module

import csv  # importing the csv module

from urllib.request import urlretrieve  # importing the urllib module

token = 'EAAK7kMLtwokBACZB1EwQOBF1I9o0ZAZBZCZBnAAAS2Pja27ev4rlr6RexlRuEvNEHX5OHXaZAMW6NjH9BbqxhJHUDqjg62UBDRBzPviCRMFnPzCbTeGwZAMM31ZBiZBMVPPdHRXSwLG8sDPkqoB88zgEYA84aFCE6ZBT3LvTUJfHRC0C6uBMHU6KDP05ZCdjpsZAv6YQRCZBZCR376m8VggSFqX7cRhyVOW3efx1MZD'


class fbdat():
    # for getting user_name.
    global token
    name = 'https://graph.facebook.com/v3.2/me?fields=id,name&access_token=' + token  # using token for getting user_name.
    n = requests.get(name)  # getting user name by using requests library.
    user_name = (n.json())  # user_name is stored.

    # for getting photos link and downloading them.
    photos_link = 'https://graph.facebook.com/v3.2/me?fields=posts{picture}&access_token=' + token  # using the token for getting links
    q = requests.get(photos_link)  # getting links by using requests library
    r = (q.json())  # photo links are stored and can be read by using .json()
    l = len(r['posts']['data'])

    # opening csv file to store links
    with open('photos.csv', 'w') as photos:  # opening a csv file with name photos in write mode
        fwrite = csv.writer(photos)
        fwrite.writerow(['links of posts'])  # first row of csv file
        i = 0
        print("started downloading photos")
        path_address = "/home/nineleaps/PycharmProjects/projects/facebook_posts/img"
        for i in range(l - 1):  # using for loop to get each link form the result (dictionary will be returned)
            p = ([(r['posts']['data'][i])['picture']])
            fwrite.writerow([r['posts']['data'][i]['picture']])  # writing remaining rows of csv file (links)
            urlretrieve(p[0], path_address + str(
                i) + ".jpg")  # using urlretrieve for getting the photos and downloading to the given path
            i = i + 1
        photos.close()  # closing the csv file
        print("downloaded pics and links are stored")


f = fbdat()
