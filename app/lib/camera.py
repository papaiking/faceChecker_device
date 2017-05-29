"""
@Author: Thuc VX<vxthuc@labsofthings.com>
@ORG: labsofthings.com
@date: 29 May 2017

Purpose: This package capture image and check wheather it contains any face in it.
"""


class Camera:

    def __init__(self, config):
        self.config = config


    def captureFaceimage(self, withFace=True):
        # Capture image from camera
        
        imgFile = './imgs/2017-05-29/118.70.217.99_1496045681.88764_image201610280001.jpg'
        

        # Check weather image contains any face in it
        if withFace and not(self._containFace( imgFile )):
            imgFile = None

        return imgFile

    def _containFace(self, imgFile):

        return True
