import requests
import json
import time
import zipfile

class Flickr:


    def __init__(self, db = None):
        self.db = db


    def clean_data(self, reponse_data):
        json_data = []
        for photo in reponse_data['photos']['photo']:
                
            data = {}
            data["id"] = photo["id"]
            data["title"] = photo["title"]
            data["owner"] = photo["owner"]
            data["ownername"] = photo["ownername"]
            data["dateupload"] = photo["dateupload"]
            data["datetaken"] = photo["datetaken"]
            data["lastupdate"] = photo["lastupdate"]
            data["views"] = photo["views"]
            data["accuracy"] = photo["accuracy"]
            data["latitude"] = photo["latitude"]
            data["longitude"] = photo["longitude"]
            data["media"] = photo["media"]

            data["encounter"] = {
                            "locationIDs": [], #[Wildbook]
                            "dates": [], #[Wildbook]
                        }
            data["animalsID"] =  [] #[Wildbook]
            data["curationStatus"] =  None #[Wildbook]
            data["curationDecision"] = None #Wildbook]

            data["gatheredAt"] =  time.ctime()
            data["relevant"] = None
            data["wild"] = None
            data["type"] = "flickr"

            
            try:
                data["url_l"] = photo["url_l"]
            except:
                data["url_l"] = ""
            data["tags"] = photo["tags"]
            data["description"] = photo['description']['_content']
            json_data.append(data)
        return json_data

    def search(self, q, date_since="2019-12-01", saveTo=False):
        print("Hello!!")
    ##AFRICA BBOX - FOR GIRAFFES - TO DO: modify search() params to allow easy insert for bounding box coordinates 
#         base_url = '''https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=6ab5883201c84be19c9ceb0a4f5ba959&text={text}&min_taken_date{min_date}&extras=description%2Cdate_upload%2C+date_taken%2C+owner_name%2C+last_update%2C+geo%2C+tags%2C+views%2C+media%2C+url_l&page={page}&bbox= -18.615646%2C-34.936608%2C50.993729%2C35.266926&format=json&nojsoncallback=1'''

        base_url = '''https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=6ab5883201c84be19c9ceb0a4f5ba959&text={text}&min_taken_date{min_date}&extras=description%2Cdate_upload%2C+date_taken%2C+owner_name%2C+last_update%2C+geo%2C+tags%2C+views%2C+media%2C+url_l&page={page}&format=json&nojsoncallback=1'''
        
        keyword = q.replace(' ','+')
        json_data = []
        url = base_url.format(text=keyword,min_date=date_since,page='1') #tags=keyword
        r = requests.get(url)
        print(r)
        response_data = r.json()
        data = self.clean_data(response_data)
        json_data.append(data)
        pages = response_data['photos']['pages']
        print(pages,'Found with',keyword)
        for page in range(2, pages+1):
            #print('page no.',page)
            url = base_url.format(text=keyword,min_date=date_since,page=str(page)) #tags=keyword
            r = requests.get(url)
            try:
                response_data = r.json()
            except JSONDecodeError:
                print("r: ", r)
            data = self.clean_data(response_data)
            json_data.append(data)
        
        print('Done Retrieving Flickr Results')
        return json_data
    
    #method to get user locations with flickr.people.getInfo()
    def getUserLocations(self, ownerIdDicts):
        owner_locations_dicts = []
        for item in ownerIdDicts:
            #get people.getInfo response from flickr api
            base_url = "https://www.flickr.com/services/rest/?method=flickr.people.getInfo&\
                        api_key=b3fb43d7040c83c55121688a2de47b1f&user_id={}&format=json&nojsoncallback=1"
            
            user_id = item['user_id'].replace('@', '%40')
            url = base_url.format(user_id)
            r = requests.get(url)
            response = r.json()
            try:
                user_location = response['person']['location']['_content'] #for photo in response['photo']
            except KeyError:
                user_location = None
            #add user loc to dictionary
            item['user_location'] = user_location
        return ownerIdDicts
    
            


