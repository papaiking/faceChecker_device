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
import dlib

from init import Log

class Camera:

    def __init__(self, config):
        self.config = config

        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (640, 480)
        self.camera = camera

        # Dlib init the detector
        self.detector = dlib.get_frontal_face_detector()

	
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
        rawCapture = PiRGBArray(self.camera, size=(640, 480))
        self.camera.capture(rawCapture, format="bgr")
        bgrImg = rawCapture.array

        # Check weather image contains any face in it
        if withFace and not(self._containFace( imgFile )):
            # Detect face in image. If there is no image, return None
            # The 1 in the second argument indicates that we should up the image
            # 1 time.  This will make everything bigger and allow us to detect more
            # faces.
            rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
            dets, scores, idx = self.detector.run( rgbImg, 1 )
            if not(scores) or len(scores)==0:
                return None

        # Save image int file
        imgFile = self._generateImageFileName()
        try: 
            cv2.imwrite(imgFile, bgrImg)
        except IOError:
            Log.error('Error in saving image to file: ' + imgFile) 

        return imgFile

