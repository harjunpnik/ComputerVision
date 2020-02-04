# Face Detection and Recognition

Create a script in OpenCV-Python that recognizes from a video stream (either webcam or saved video file) and frames your own face in real time! So-called "false positives" should be avoided, ie if your own face is missing from the video stream, the program should not point out anyone else's face.

* First detect all faces in each frame, including by Haar-Cascading (Viola-Jones algorithm) 
* Apply LBPH (Low Binary Pattern Histograms) to identify your face

