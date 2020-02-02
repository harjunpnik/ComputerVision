# Simple identification of geometric figures

##  Create a script in OpenCV-Python that can identify hexagons, triangles, rectangles, squares in attached image "shapes.jpg"

Have the script draw the outlines around the found figures and display a "text label" at each found figure describing the type of figure. To draw / highlight the outline around a figure, you can use cv2.drawContours. To print print "text labels" you can use cv2.putText. Check the OpenCV-Python manual for more info!

The solution can be simplified in such a way that you assume in the script that if a found closed contour has:

* 3 corners => triangle
* 4 corners => rectangle or square
* 6 corners => hexagon

To find out if a found quadrilateral is a square or a rectangle, you can use the cv2.boundingRect function (give the contour of the quadrilateral as a parameter) to examine the width and height of the quadrilateral. If the width is about the same as the height, you can assume that it is a square, otherwise a rectangle!