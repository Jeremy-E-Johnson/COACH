# COACH
Instant replay system. Designed to be used with a webcam and an Ubuntu VM.


This program is designed to provide instant replay functionality on Linux.

THe goal is for self criticism of form during sporting events. Recorded sequences can be played slowly or even in reverse for anlysis.


To run this project you need:

Python3 (with numpy)
OpenCV (with python bindings)

For example, on Ubuntu, you can run:

sudo apt install python3
sudo apt install python3-opencv
pip3 install numpy

Then,

python3 playback.py

should work. Webcamera issues can be difficult. Ensure that you have access to a webcam by testing with software such as camorama and cheese.
