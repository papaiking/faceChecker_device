from rtimer import RepeatedTimer

import time


class FaceChecker:
    
    def __init__(self, options, config):
        self.options = options
        self.config = config
        
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

        # Search for image

        # Send event if happening


