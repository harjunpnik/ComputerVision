# Edge enhancement and edge detection

## 1. Apply the following 2D Laplacian sharpening filter mask to any image of your choice 

|    |    |    |  
|--- |--- |--- |
| 0  | -1 | 0  |
| -1 |  5 | -1 | 
| 0  | -1 | 0  |

Choose an image with plenty of edges and structure, i.e., buldings or monuments. Include in your report a screen shot of the orignal as well as the filtered image and comment on your findings. 

## 2. Apply the following Sobel horizontal (row) and vertical (column) edge detector mask to an image of your choice (use the same image as for #1)
Horizontal

|    |    |    |  
|--- |--- |--- |
| 1  | 2 | 1  | 
| 0 |  0 | 0 | 
| -1  | -2 | -1  |

Vertical

|    |    |    |  
|--- |--- |--- |
| -1  | 0 | 1  |
| -2 |  0 | 2 | 
| -1  | 0 | 1  |

For this purpose you can again define the above mentionded masks and use the cv2.filter2D function or alternatively the cv2.Sobel function where the horizontal edge and vertical edge detector masks are already defined. Try both! Include in your report a screen shot of the orignal as well as the edge map and comment on your findings. 

## 3. How would you implement an edge detector for the attached image face.jpg in order to achieve the "best possible" result? 

Now based on what you have learned from the image processing lectures series so far, how would you implement an edge detector for the attached image face.jpg in order to achieve the "best possible" result? 

Apply a combination of suitable image processing techniques before performing the actual edge detection. Also, you may think about including some post-processing after edge detection as well to enhance the edges.  You decide as there is no right/wrong solution!!