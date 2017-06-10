# About module

This is one module in FaceChecker application at: [http://labsofthings.com/facechecker](http://labsofthings.com/facechecker)

Repository: [https://github.com/papaiking/faceChecker_device.git](https://github.com/papaiking/faceChecker_device.git)

This module is installed in Camera hub to do following tasks:

-   Request server to get [LINKEDFACE++](http://plusplus.linkedface.com/)'s access token
-   Periodically capture image from camera, and call [LINKEDFACE++](http://plusplus.linkedface.com/) to search for user profile 
-   If there is a profile founded, send it to server to make new event

# Install software

### Free up some space on your micro SD Card
This module needs: 

-   About 1 Gb for installing OpenCV 2.4
-   And space for storing image captured from Camera

If space left in SD card is not enough, you can free up by removing: Wolfram & LibreOffice in Raspbian OS. After this step, you can add more 1 GB space.

-   Wolfram (658 MB)
-   libreoffice (253 MB)

Try commands:
```
sudo apt-get purge wolfram-engine
sudo apt-get clean
sudo apt-get autoremove

sudo apt-get remove --purge libreoffice*
sudo apt-get clean
sudo apt-get autoremove
```

Reference: [http://raspi.tv/2016/how-to-free-up-some-space-on-your-raspbian-sd-card-remove-wolfram-libreoffice](http://raspi.tv/2016/how-to-free-up-some-space-on-your-raspbian-sd-card-remove-wolfram-libreoffice)

### Install OpenCV and Python on your Raspberry Pi 2 B+

This step takes very long time - more than 1 hour to install OpenCV. We used Python 2.7.9 and OpenCV 2.4.11. Fortunately, there are some good documents for installing Python 2.7.9 and OpenCV 2.4 on Raspbian here:

-   [http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/](http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/)
-   [http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html](http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html)
-   [http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/](http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/)

### Install FaceChecker-Device

Download module from repository: [https://github.com/papaiking/faceChecker_device.git](https://github.com/papaiking/faceChecker_device.git)

Go to folder `~/facechecker`  and type command to download module:

`pi@raspberrypi:~ $ git clone https://github.com/papaiking/faceChecker_device.git`

Go to module folder and type command to install dependencies:

`pip install -r dependency.txt`

You can follow below references to install dependencies manually:

-   configparser: [https://pypi.python.org/pypi/configparser/](https://pypi.python.org/pypi/configparser/)
-   PYTHON PICAMERA: [https://www.raspberrypi.org/documentation/usage/camera/python/README.md](https://www.raspberrypi.org/documentation/usage/camera/python/README.md)


# Configuration 

### Register device
Use Administration application, access to device management to register device. After this step, you.ve got an TOKEN for you device ((Refer to Administration application))

### Setting values

Go to project folder, and open file: `faceChecker_device/app/config/facechecker.cfg`
``` 
  1 [DEFAULT]
  2 CHECKING_INTERVAL = 2
  3 IDLE_INTERVAL = 180
  4 IMG_LOCATION = /home/pi/facechecker/faceChecker_device/imgs
  5 HAAR_CASCADE = cv2/haarcascade_frontalface_default.xml
  6
  7 [Server]
  8 FaceChecker_TOKEN = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVjOTQyNjc0YzkyZGFlMmY0ZjcwOTk0ZTBkNWQ1ZjU4IiwiYWRkcmVzcyI6Ik5vIDgsIFRyYW5nIFRoaSwgSG9hbiBLaWVtLCB    IYW5vaSIsInNlY3JldCI6IjZnZmhnZmhmIiwic3RhdHVzIjowLCJhYm91dCI6IkNhbWVyYSBmb3Igb2ZmaWNlIiwiY3JlYXRlZCI6IjIwMTctMDUtMThUMTU6MjI6MzAuMDAwWiIsImlhdCI6MTQ5NTI3MDcxNX0.41E    RZl1CISqPOMxT7T6Kq0zpJ-uT_HHt1meHexw_BmI
  9 FaceChecker_GET_LINKEDFACE_TOKEN = http://118.70.151.36:9100/gateway/linkedface_token
 10 FaceChecker_EVENT = http://118.70.151.36:9100/gateway/add_event
 11
 12 [Linkedface]
 13 LINKEDAFCE_img_server = https://api.linkedface.com/search/imgs/ 
 14 LINKEDAFCE_postimg = https://api.linkedface.com/post/create 
 15 LINKEDAFCE_search = https://api.linkedface.com/app/search/
```

Update appropriate values.

-   CHECKING_INTERVAL: the interval time in second that device will capture image and processing data
-   IDLE_INTERVAL: if there is any user found in camera, device will stop checking camera for IDLE_INTERVAL second. After this time, device continue checking again.
-   IMG_LOCATION: folder in device that store image files that captured from camera
-   HAAR_CASCADE: pre-trained facial model data, used by OpenCV to detect face in image
-   FaceChecker_TOKEN: is token, that FaceChecker server generated for device. Device uses this token to access FaceChecker.s services. You got it after registering in the first step configuration.
-   FaceChecker_GET_LINKEDFACE_TOKEN: url of FaceChecker.s services that returns Linkedface++.s access token (Refer to Application server)
-   FaceChecker_EVENT: url of FaceChecker.s services that is used to send event to server


# Run module

`./bin/facechecker [-f frequency] [-i idle_time]`

If you specify `frequency` and `idle_time` it will overwrite default values `CHECKING_INTERVAL` and `IDLE_INTERVAL` in configuration file
