"""
@Author: Thuc VX<vxthuc@labsofthings.com>
@ORG: labsofthings.com
@date: 29 May 2017

Purpose: This package capture image and check wheather it contains any face in it.
"""
from datetime import datetime
import os

from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2

from init import Log

class Camera:

    def __init__(self, config):
        self.config = config

        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (800, 600)
        self.camera = camera

        # Init harr casscade 
        script_dir = os.path.dirname( os.path.realpath(__file__) )
        harr_file = os.path.join( script_dir, '..', self.config['DEFAULT'].get('HAAR_CASCADE') )
        #Log.info('Harr casscade file: ' + harr_file)
        self.harr_detector = cv2.CascadeClassifier( harr_file )

	
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
        
        fileName = os.path.join( img_dir, 'facechecker_' + time_now.strftime("%H-%M-%S-%f") + '.jpg') 			
        return fileName

	# Capture and check face in image
    def captureFaceimage(self, withFace=True):
        # grab an image from the camera
        rawCapture = PiRGBArray(self.camera)
        self.camera.capture(rawCapture, format="bgr")
        bgrImg = rawCapture.array
        #Log.info('Image size: ' + str(len(bgrImg)))

        if withFace:
            # Detect face in image. If there is no image, return None
            grayImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2GRAY)
            faces = self.harr_detector.detectMultiScale ( 
                grayImg, 
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(100, 100),
                flags = cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            #Log.info('Number of faces: ' + str(len(faces)))
            if (faces is None) or len(faces)==0:
                return None

        # Save image int file
        imgFile = self._generateImageFileName()
        try: 
            cv2.imwrite(imgFile, bgrImg)
        except IOError:
            Log.error('Error in saving image to file: ' + imgFile) 

        return imgFile

