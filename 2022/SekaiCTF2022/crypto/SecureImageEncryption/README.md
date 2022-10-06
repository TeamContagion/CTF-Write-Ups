# SecureImageEncryptionWriteup
## Idea
The idea to solve this CTF challenge came from a research paper made on the topic.
https://ieeexplore.ieee.org/abstract/document/7295616 
The idea of solving it is to feed the encryption webpage 2 linear grayscale images. One of them is horizontal and the other one is vertical. They are attached in the repo. This works because the grayscale value of each pixel can be used to map the orignal location of that pixel.
It is a coordinate system where image one indicates y and image 2 indicates x.
gradient 1
    ![alt text](gradient1.png)

gradient 2
    ![alt text](gradient2.png)
## Solution
The python program creates a list using the encrypted image and the values of each pixel.
Then a new image is created and it gets the values of that list in order.
The value of the pixel at index i is obtained and is placed at the location indicated by the grayscale values at index i.
This repeats for every pixel in the image.
