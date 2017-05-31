from rtimer import RepeatedTimer
from search import Search
from init import Log
from event import Event
from camera import Camera

import json
import time


class FaceChecker:
    
    def __init__(self, options, config):
        self.options = options
        self.config = config
        self.search = Search(options, config)
        self.event = Event(config)
        self.camera = Camera(config)

        #Log.info( 'Linkedface token is: ' + self.search.linkedface_token )

    """
    This function create a timer with checkpoint function. 
    A function for capturing image and searching user.
    Then starting timer to run checkpoint periodically 
    """ 
    def start(self):
        timer = RepeatedTimer(self.options, self.checkPoint)
        timer.start()

    """
    Start to check event: capture image, search and then send event
    """
    def checkPoint(self):
        #Log.info ('Start a check point')
        # Capture image
        captured_img = self.camera.captureFaceimage( withFace=True)
        if captured_img is None:
            return False
        Log.info('Captured face image: ' + captured_img)

        # Search for image
        search_res = self.search.searchUser(captured_img)      
        if (search_res is not None) and (search_res.get('status')==1):
            #Log.info('Search response: ' + json.dumps(search_res))
            # Send event if happening
            self.event.sendEvent(search_res.get('sample'), search_res.get('profiles')[0])
            return True
        else:
            return False

