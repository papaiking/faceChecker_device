"""
@Author: Thuc VX<vxthuc@labsofthings.com>
@ORG: labsofthings.com
@date: 29 May 2017

Purpose: This package works on event.
It reads search result and create event then send to FaceChecker server
"""

import time
import requests
import json

from init import Log


class Event:
    
    def __init__(self, config):
        self.config = config


    def _createEvent(self, evidence, profile):
        if (profile is None) or (evidence is None):
            return None

        event = {
            "user_id": profile.get('id'),
            "name": profile.get('name'),
            "picture": profile.get('picture'),
            "similarity": profile.get('similarity'),
            "event_picture": self.config['Linkedface'].get('LINKEDAFCE_img_server') + evidence.get('fileName'),
            "type": 1,
            "valid": 1
        }
        return event

    def sendEvent(self, evidence, profile):
        event_url = self.config['Server'].get('FaceChecker_EVENT')
        if event_url is None:
            Log.error('Error in configuration for parameter: FaceChecker_EVENT')
            return None

        data = self._createEvent( evidence, profile )
        if data is None:
            return None
        
        token = self.config['Server'].get('FaceChecker_TOKEN')
        if token is None:
            Log.error('Error in configuration for parameter: FaceChecker_TOKEN')
            return None
           
        headers = {'x-access-token':token, 'Content-Type':'application/json'}

        # Log.info('Header: ' + json.dumps(headers) + ', url: ' + event_url + ', event: ' + json.dumps(data))
        res = requests.post( event_url, headers=headers, data=json.dumps(data) )
        if not(res) or res.status_code != 200:
            return None

        return res.json()

