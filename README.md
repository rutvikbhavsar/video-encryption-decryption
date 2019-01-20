# video-encryption-decryption
The main goal of the project is to perform encryption and decryption on videos without requiring any camera modifications.

To properly detect objects in the video, Region Update algorithm is used. This algorithm deals with the loss and error drifting of motion caused by the video encryption. To detect motion related information, bitstreams and codeword length is used. Object motion occurring on videos are continuous in space and time (we mean that for a short amount of period the detected object does not leave the frame and is being processed by the proposed algorithm), and Region Update algorithm is based on these priors of physics.  

One major limitation of the proposed system is the loss of audio.
