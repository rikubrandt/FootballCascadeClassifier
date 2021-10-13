#!/usr/bin/bash/python3

import cv2 as cv
import sys
import argparse


def extract(pathIn, pathOut, name, interval):
    num, count = 0, 0
    video = cv.VideoCapture(pathIn)
    frames = cv.CAP_PROP_FRAME_COUNT
    print(frames)
    success, frame = video.read()
    success = True
    oldFrame = None
    while success:
        video.set(cv.CAP_PROP_POS_MSEC, (count*1000))
        print(video.get(cv.CAP_PROP_POS_MSEC)) 
        if oldFrame == video.get(cv.CAP_PROP_POS_MSEC):
            break
        oldFrame = video.get(cv.CAP_PROP_POS_MSEC)
        success, frame = video.read()
        cv.imwrite(pathOut + "//%s%d.jpg" % (name, num), frame)
        count += interval
        num += 1
    cv.destroyAllWindows()


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("pathIn", help="Path to video.")
    a.add_argument("pathOut", help="Path where images are to be saved.")
    a.add_argument("name", help="Custom name for the saved images.")
    a.add_argument("interval", help="Interval of pictures taken.")
    args = a.parse_args()
    print(args)
    extract(args.pathIn, args.pathOut, args.name, int(args.interval))



