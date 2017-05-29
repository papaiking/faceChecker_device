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
import requests
import json

from init import Log


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

    # Check if image contain any face
    def _validateFaceImage(self, captured_img):
        # TODO here

        return True

    # Upload image for searching 
    def _uploadImage(self, captured_img):

        imgFile = open(captured_img, 'rb')
        if imgFile is None:
            Log.error('Cannot open image file: ' + captured_img)
            return None

        upload_url = self.config['Linkedface'].get('LINKEDAFCE_postimg')        
        files = { 'faceImage': imgFile }
        res = requests.post( upload_url, files=files ) 

        if res is not None and res.status_code==200:
            #Log.info('Uploaded file: ' + res.text)
            return res.json()
        else:
            Log.error('Error in uploading image for searching')
            return None
    
    """
    This function is for searching users that have similar face in image
    It does following steps:
        - Check if this image is valid, contain face
        - Upload image for searching
        - Search and return result
    """
    def searchUser(self, captured_img):
        # Check wheather this is a valid image

        # Upload image for searching
        uploaded_img = self._uploadImage(captured_img)
        # Log.info('Uploaded image: ' + json.dumps(uploaded_img))
    
        if uploaded_img is not None:
            # Search for user in image
            search_url = self.config['Linkedface'].get('LINKEDAFCE_search')
            if search_url is None:
                Log.error('Error in configuration for parameter: Linkedface.LINKEDAFCE_search')

            search_url = search_url + uploaded_img.get('id')
            headers = {'Authorization':'BEARER ' + self.linkedface_token}
            #Log.info('Search URL: ' + search_url + ', header: ' + json.dumps(headers)) 
 
            # Request for searching
            res = requests.get(search_url, headers=headers)
            if res.status_code == 200:
                #Log.info('Search response: ' + res.text)
                return res.json()
            else:
                Log.info('Error in searching user: ' + res.text)
                return None
        else:
            return None

