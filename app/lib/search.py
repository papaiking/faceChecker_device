"""
@Author: Thuc VX<vxthuc@labsofthings.com>
@ORG: labsofthings.com
@date: 27 May 2017

Purpose: This package is for search for user in captured image.
It does some processing: 
    - Request to get Linkedface token, 
    - Post search image to Linkedace, 
    - Ssearch user appear in image
"""

import time
from init import Log
import requests

class Search:
    
    def __init__(self, options, config):
        self.options = options
        self.config = config
        self.linkedface_token = self.getLinkedface_token()

    # Call to FaceChecker server to get Linkedface access token
    def getLinkedface_token(self):
        # Get and check token URL
        token_url = self.config['Server'].get('FaceChecker_GET_LINKEDFACE_TOKEN')
        if not( token_url ):
            Log.error('Configuration: FaceChecker_GET_LINKEDFACE_TOKEN for URL to get Linkedface token is invalid')
            return None
        
        # Get and check server token
        server_token = self.config['Server'].get('FaceChecker_TOKEN')
        if not( server_token ):
            Log.error('Configuration: FaceChecker_TOKEN to access server APIs is invalid')
            return None
        headers = {'x-access-token': server_token}

        # Request to get Linkedface token
        ret = requests.get(token_url, headers=headers)
        if not(ret) or (ret.status_code != 200):
            Log.error('Cannot request to server to get Linkedface token')
            return None
        data = ret.json()
        # return Linkedface access token
        return data.get('token')


    #def upload_image(self, captured_img):



        
    #def search(self, captured_img):
        #captured_img = '2017-05-26/118.70.217.99_1495781429.20515_image201610280001.jpg'


