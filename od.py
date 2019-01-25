# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# from PyQt4 import QtGui
# import tkinter
import numpy as np
import os, sys
import argparse
import cv2 as opc


def object_detection():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("-a", type=int)
    psr_holder = vars(parser.parse_args())

    check = True
    min = 80    #Best minimun threashold to detect far sited object is 38 else 45.
    max = 255
    f = psr_holder["file"]

    # Turns on webcam if video file is not provided via prompt.
    if psr_holder.get("file", None) is None:
        webcam = opc.VideoCapture(0)  #Used '0' for in-built webcam, if you have external camera change it to '1'.)
    else:
        webcam = opc.VideoCapture(f)

    init_f = None #Initialise frame for the feed.

    try:
        if check:
            while check is True: #Go through each frame.
                (found, v_frm) = webcam.read()
                v_frm = opc.resize(v_frm, (640, 480), interpolation=opc.INTER_LINEAR)
                if not found:  break  #If reached end of the input frames.
                f = opc.cvtColor(v_frm, opc.COLOR_BGR2GRAY)

                f_blur = opc.GaussianBlur(f, (15, 15), 0) #Blurring and smoothing the frame.

                try:
                    if init_f is None:
                        init_f = f_blur
                except ValueError:
                    pass

                diff = opc.absdiff(init_f, f_blur, v_frm) #Substract the first frame and the current frame.
                t_hold = opc.threshold(diff, min, max, \
                                       opc.THRESH_BINARY)[1]
                count_c = []

                def cmain():
                    for m in count_c:
                        hold = m
                        return hold
                    cmain()

                t_hold = opc.dilate(t_hold, None, iterations=10)
                temp, count_c, temp = opc.findContours(t_hold.copy(), \
                                      opc.RETR_EXTERNAL, opc.CHAIN_APPROX_SIMPLE)
                                    #opc.CHAIN_APPROX_SIMPLE saves memory.


                for i in count_c:   #Go through each found boudries knoow as contours.
                    c_area = opc.contourArea(i)
                    try:
                        if c_area <= 500: continue
                    except ValueError:
                        pass
                    a, b, h, w = opc.boundingRect(i)   
                    opc.rectangle(v_frm, (a, b), \
                                  (a + w, b + h), (0, 255, 0), 2)  


                    rect = opc.minAreaRect(i)
                    red_b = opc.boxPoints(rect)
                    red_b = np.int0(red_b)
                    opc.drawContours(v_frm, [red_b], 0, (0, 0, 255), 1)   

        

                wait = None
                opc.imshow("Decting objects via webcam " + "\r\r\r\r\r\r\r\r\r*****Press ESC button to EXIT*****", v_frm)
                wait = opc.waitKey(2) & 255

                if wait == 27:  #27 Esc button.
                    exit()
    except:
        raise  Exception("Unfortunately fed input could not be processed!, Please insert a proper file name.")

    webcam.release()
    opc.destroyAllWindows()


if __name__ == '__main__':
    object_detection()
