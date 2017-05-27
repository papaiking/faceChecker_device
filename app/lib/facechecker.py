from rtimer import RepeatedTimer
from search import Search
from init import Log

import time


class FaceChecker:
    
    def __init__(self, options, config):
        self.options = options
        self.config = config
        search = Search(options, config)

        Log.info( 'Linkedface token is: ' + search.linkedface_token )

    """
    This function create a timer with checkpoint function. 
    A function for capturing image and searching user.
    Then starting timer to run checkpoint periodically 
    """ 
    def start(self):
        timer = RepeatedTimer(self.options, self.checkPoint)
        timer.start()

        #self._get_prams()
        
        #return

    def _get_prams(self):
        #print self.process.execute("date")
        print (time.strftime("%H:%M:%S"))
        print ('frequency: ' + str(self.options.checking_interval) )
        print ('frequency: ' + str(self.options.idle_internal) )

        print ('Linkedface search: ' + self.config['Linkedface'].get('LINKEDAFCE_search') )

    def checkPoint(self):
        print ('Start a check point')
        # Capture image
        captured_img = '2017-05-26/118.70.217.99_1495781429.20515_image201610280001.jpg'

        # Search for image




        # Send event if happening


