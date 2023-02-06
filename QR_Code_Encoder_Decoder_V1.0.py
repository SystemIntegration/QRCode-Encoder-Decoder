#!/usr/bin/env python
# -*-coding:utf-8 -*-
#
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
# File          : QR_Code_Encoder_Decoder_v_1.0.py
# Author        : BMV System Integration Pvt Ltd.
# Version       : 1.0.0
# Date          : 17th January 2023
# Contact       : info@systemintegration.in
# Purpose       : This is the python script to encode and decode the QRCode.
# import        : qrcode - to encode the QRCode.
#                 cv2    - to decode the QRCode.
#                 os     - to do os related operations.
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------

import qrcode
import os
import cv2

img_dir = os.path.dirname(__file__)
en_qr = os.path.join(img_dir, "qr.png")
sample_qr = os.path.join(img_dir, "sample_QR.png")

def qr_Encoder(data, imgpath=en_qr):
    """
    Function to encode the QRCode.

    Param : data - data to encode into QRCode.
            imgpath - the path of the QR image.

    Returns : path of the encoded QRCode image.
    """
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data) # add data to the instance.
        qr.make(fit=True) # make the QRCode of the data    
        qrimg = qr.make_image(fill_color = 'black', back_color='white') # get the image object of QRCode.
        qrimg.save(imgpath) # save the QRCode image.

        return imgpath
    except Exception as e:
        return None

def qr_Decoder(qr_image=en_qr):
    """
    Function to decode the QRCode.

    Param : qr_image - path of the QRCode image.

    Returns : Decoded of the QRCode.
    """
    try:
        imdata = cv2.imread(qr_image) # read the QRCode image.
        det = cv2.QRCodeDetector() # QRCode Detctor object
        retval , points, s_qr = det.detectAndDecode(imdata) # Detect and decode QRCode.
        if points is not None:
            return retval
        else:
            return None
    except Exception as e:
        return None

if __name__ == "__main__":
    qr_image = qr_Encoder("BMVSI Pvt. Ltd.")

    if qr_image is not None and os.path.exists(qr_image):
        print("Encoded QRCode : ", qr_image)
        
    else:
        print("Not able to generate QRCode!!")

    # data = qr_Decoder("C:\\Users\\bmvsi-117\\Pictures\\box_sorting-pick_n_place") # image without QRCode.
    data = qr_Decoder()
    if data is None:
        print("No QRCode Detected!!")
    else:
        print("Decoded Data : ", data)