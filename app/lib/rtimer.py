"""
@Author: Thuc VX<vxthuc@yahoo.com>
@ORG: labsofthings.com
@date: May 11, 2017 

Purpose: This is repeated timer. Can run repeatedly
"""

from threading import Timer

class RepeatedTimer(object):
    def __init__(self, options, function, *args, **kwargs):
        self._timer     = None
        self.options    = options
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        #self.start()

    def _run(self):
        self.is_running = False
        self.found = False
        self.found = self.function(*self.args, **self.kwargs)
        self.start()

    def start(self):
        if not self.is_running:
            interval = self.options.checking_interval
            self._timer = Timer( interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
