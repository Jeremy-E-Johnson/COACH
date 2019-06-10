import cv2
import numpy as np
import time
import sys

def play_video(frames, mspf, rate=1.0, frame='frame'):
    fc = len(frames)
    mspf = mspf * (1/rate)

    for i in range(0, fc):
        cv2.imshow(frames[i], frame)
        cv2.waitKey(int(mspf))


def record_video_fc(fc, display='frame', device=0):
    frames = [None]*fc

    cap = cv2.VideoCapture(device)

    start = time.time()
    for i in range(0, fc):
        ret, frame = cap.read()
        frames[i] = frame

        if display is not None:
            cv2.imshow(display, frame)

        cv2.waitKey(1)
    end = time.time()
    mspf = ((end - start)/fc) * 1000

    cap.release()

    return frames, mspf


def save_video(frames, mspf, filename):
    size = frames[0].size

    writer = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, writer, int(1/mspf), size0)

    for frame in frames:
       out.write(frame)

    out.release()


def nothing(x):
    pass


cap = cv2.VideoCapture(0)
run = False
frames = []
MAX_FRAMES = 100

def record(event, x, y, flags, param):
    global run
    global frames

    if event == cv2.EVENT_LBUTTONDOWN:
        run = not run

        if run:
            frames = []
        while run:
            frame = cap.read()[1]
            frames.append(frame)
            cv2.imshow('main', frame)
            cv2.waitKey(1)
            if len(frames) > MAX_FRAMES:
                 run = False

        current = 0
        while not run:
           if current < len(frames) and current >= 0:
               cv2.imshow('main', frames[current])
               rate = cv2.getTrackbarPos('rate', 'main') - 100
               #rate = 1 + (1/(0.001*rate + 0.1))
               ms = 10 + 100 - abs(rate)

               cv2.waitKey(ms) #  ms can not be 0 because of bound on slider
               if rate >= 0:
                   current += 1
               else:
                   current -= 1
           elif current >= len(frames):
               current = 0
           else:
               current = len(frames) - 1



def main():
    cv2.namedWindow('main')
    cv2.createTrackbar('rate', 'main', 100, 200, nothing)
    cv2.setMouseCallback('main', record)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    cv2.waitKey(1)


if __name__ == "__main__":
    main()
