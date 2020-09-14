from google_images_search import GoogleImagesSearch
import os
import requests

with open(r".\APIKEY.txt" , 'r') as f:
    f_con = f.readlines()
    APIKEY, api2 = f_con[0],f_con[1]
gis = GoogleImagesSearch(APIKEY, api2)

class searcher:
    def __init__(self,word,imgName):
        self.word = word
        self.imgName = imgName
        self.search_params = _search_params = {
        'q': word,
        'num': 1,
        'safe': 'high',
        'fileType': 'png',
        'imgType': 'photo'
        }
    def getImage(self):
        gis.search(search_params=self.search_params)

        try:
            os.remove("secret.jpg")
        except :
            pass
        gis.search(search_params=self.search_params,path_to_dir='.',custom_image_name=self.imgName)












