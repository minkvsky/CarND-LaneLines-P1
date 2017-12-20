# **Finding Lane Lines on the Road**

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.
steps as following:
- converte the images to grayscale
- blur the gray image with gaussian_blur
- apply canny edge detection to the blured image
- generate a region_of_interest and mask almost everything in the image except the lane lines
- implement a Hough transform on masked edge detected image then get some lines
- draw_lines:
  - find the two longest line segment with different direction
  - find the four intersection points of the two lines with the region_of_interest.
  - get two new lines from the four points
  - then draw the two new lines.

here is the output result:

![test_images](test_images_output/test_images.jpg)


### 2. Identify potential shortcomings with your current pipeline

potential shortcoming:
- lane lines don't always occur in the region of interest.
- lane lines maybe disappear somewhere.
- pavement may distube the detection.
- more lane lines(not only two) will appear.

### 3. Suggest possible improvements to your pipeline

possible improvements:
- dynamic region of interest base on the image.
- more lines should be got then algorithm select two lines base on the relation of lines.
