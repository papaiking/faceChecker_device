# General information #

This module is installed in Camera hub, runs under Python.

This module do following tasks:

-   Request to server to get LINKEDFACE.s access token
-   Periodically capture image from camera, and call to LINKEDFACE to search for user profile 
-   If there is a profile founded, send it to server to make new event


# Installation software #

## Free up some space on your micro SD Card ##
This module needs: 

-   About 1 Gb for installing OpenCV 2.4
-   And space for storing image captured from Camera

If space left in SD card is not enough, you can free up by removing: Wolfram & LibreOffice in Raspbian OS. After this step, you can add more 1 GB space.

-   Wolfram (658 MB)
-   libreoffice (253 MB)

Try commands:
`
sudo apt-get purge wolfram-engine
sudo apt-get clean
sudo apt-get autoremove

sudo apt-get remove --purge libreoffice*
sudo apt-get clean
sudo apt-get autoremove
`

Reference: http://raspi.tv/2016/how-to-free-up-some-space-on-your-raspbian-sd-card-remove-wolfram-libreoffice

## Install OpenCV and Python on your Raspberry Pi 2 B+ ##

This step takes very long time - more than 1 hour to install OpenCV. We used Python 2.7.9 and OpenCV 2.4.11. There are some good documents for installing Python 2.7.9 and OpenCV 2.4 on Raspbian here:

-   http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/
-   http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html
-   http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/

## Install FaceChecker-Device ##

Download module from repository: https://github.com/papaiking/faceChecker_device.git 

Go to home folder and type command to download module:
`pi@raspberrypi:~ $ git clone https://github.com/papaiking/faceChecker_device.git`

Go to module folder and type command to install dependency:

`pip install -r dependency.txt`

# Configuration #


# Run module #


