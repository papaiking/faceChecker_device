"""
@Author: Thuc VX<vxthuc@labsofthings.com>
@ORG: labsofthings.com
@date: 27 May 2017

Purpose: This package inits all variables for application: log, consts
"""

#!/usr/bin/env python
import logging
import logging.handlers

#from constant import CONST


# Set up a specific logger with our desired output level
Log = logging.getLogger('Linkedace_FaceChecker')
Log.setLevel(logging.DEBUG)
# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
              './logs/facechecker.log', maxBytes=20, backupCount=5)
Log.addHandler(handler)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
Log.addHandler(ch)


