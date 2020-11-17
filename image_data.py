import urllib.request
import base64
import requests

class Save():
    def __init__(self):
        return
    
    #convert urls to jpg image files
    def url_to_jpg(self, i, url, file_path):
        '''
            Args:
                -- i: number of image
                -- url: a URL address of a given image
                -- file_path: where to save the final image
        '''

        filename = 'image-{}.jpg'.format(i)
        full_path = '{}{}'.format(file_path, filename)
        urllib.request.urlretrieve(url, full_path)

        #print('{} saved.'.format(filename))
        return filename
    
    #method to get url links from json list
    def get_urls(self, json_data, demo_one_page=False):
        urls = []
        
        if(demo_one_page):
            for doc in json_data:
                if(doc['url_l'] != ''):
                    urls.append(doc['url_l'])
        
        else:
            for page in json_data:
                for doc in page:
                    if(doc['url_l'] != ''):
                        urls.append(doc['url_l'])
        return urls
    
    #convert an image using a url to its bytes representation
    def get_as_base64(self, url):
        return requests.get(url).content

    #download images from urls into jpgs in a file specified (must be in same directory as calling script)
    def download_images(self, file_path, json_data):
        
        #get all urls from json docs
        urls = self.get_urls(json_data)
        
        # Save Images to the Directory by iterating through urls
        '''store each image as a dict in list_items
           dict = {'name': img name, 
                   'url': img_url from flickr, 
                   'data': bytearray representation of img
                   }
        '''
        list_image_dicts = []
        i = 0
        
        ## if saving images to a folder           
        for url in urls:
            i += 1 
            image_name = self.url_to_jpg(i, url, file_path) #saves actual jpg image to file_path specified
            print(image_name)
            image_dict = {'name': image_name,
                           'url': url,
                           'data': self.get_as_base64(url)
                         }
            list_image_dicts.append(image_dict)

        print('done downloading images to folder!')
        
        return list_image_dicts
    
    #get results from json file
    def download_metadata(self, json_data, demo_one_page):
        print('retrieving data from json_res...')
        #get all urls from json docs
        urls = self.get_urls(json_data, True)
        i = 0
        list_image_dicts = []
        for url in urls:
            i += 1 
            image_name = 'image-{}.jpg'.format(i)
            image_dict = {'name': image_name,
                           'url': url,
                           'data': self.get_as_base64(url)
                         }
            list_image_dicts.append(image_dict)

        print('done building image dictionaries from json file!')
        
        return list_image_dicts
        