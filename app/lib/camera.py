"""
@Author: Thuc VX<vxthuc@labsofthings.com>
@ORG: labsofthings.com
@date: 29 May 2017

Purpose: This package capture image and check wheather it contains any face in it.
"""
from datetime import datetime

class Camera:

    def __init__(self, config):
        self.config = config

	
	# Generate file name for storing image
	def _generateImageFileName(self):
		img_dir = self.config['DEFAULT'].get('IMG_LOCATION')
		if img_dir is None:
			Log.error('Invalid configuration for parameter: DEFAULT.IMG_LOCATION')
			return None

		time_now = datetime.now()
		img_dir = os.path.join( img_dir, time_now.strftime("%Y-%m-%d") )
		if not os.path.exists( img_dir):
			os.makedirs( img_dir )
		
		fileName = os.path.join( img_dir, 'facechecker_time_now.strftime("%H-%M-%S-%f")', 'jpg') 			
		return fileName

	# Capture and check face in image
    def captureFaceimage(self, withFace=True):
        # Capture image from camera
        
        imgFile = self._generateImageFileName() 
        

        # Check weather image contains any face in it
        if withFace and not(self._containFace( imgFile )):
            imgFile = None

        return imgFile

    def _containFace(self, imgFile):

        return True
