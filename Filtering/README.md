# Histogram Equalization

Short report, with screenshots of the images before and after 2D filtering, the python scripts you used for filtering, as well as your comments on 1-6.

## 1. Apply the following low pass mask on LP_filter-candidate.jpg

|  1 | 1  |  1|  
|:--|:--|:--|
| 1 | 2 | 1 | 
| 1 | 1 | 1 |

with
1/10 (Scaling factor)


## 2. Apply the following high pass mask on High-Contrast.jpg

| -1 |-1  |-1  |  
|:-- |:-- |:-- |
| -1 |  9 | -1 | 
| -1 | -1 | -1 |

with
1 (Scaling factor)

## 3. Apply the Gaussian low pass filter for different smoothing (σ) values to the LP_filter-candidate.jpg image

## 4. Comment on your findings in 1-3

Giving one application where you would use each particular filter type? By comparing the Gaussian LP filter results with those you obtained in #1, explain the reason you would select a Gaussian LP filter instead of the LP mask in #1?

## 5. Apply both a 3x3 and a 7x7 median filtering mask to the attached noisy images (PictureN_medianfiltering.jpg)'

Please comment on both their noise reduction performance and state whether the larger mask is a better choice than the smaller mask.  

## 6. What happens if the median filter mask window length is increased to say 11x11 pixels?