import numpy as np
from scipy.signal import convolve2d

class Filters:

    @staticmethod
    def invert(img_array):
        """Invert image colors"""

            # Subtracting each pixel value in the image from 255 flips them:
                # Dark pixels (near 0) → bright (near 255)
                # Bright pixels (near 255) → dark (near 0)
        return 255 - img_array
    
    @staticmethod
    def threshold(img_array, thresh=128):
        """Convert to black & white"""

            # This creates a boolean mask:
                # True where pixel value > thresh
                # False where pixel value ≤ thresh
                # For True it will be multiply by 255 
        return (img_array > thresh) * 255
    
    @staticmethod
    def flip_horizontal(img_array):
        """Flip image left-right"""
        # Around the y-axis
        return np.fliplr(img_array)
    
    @staticmethod
    def flip_vertical(img_array):
        """Flip image top-bottom"""
        # Around the x-axis
        return np.flipud(img_array)
    
    @staticmethod
    def sharpen(img_array):
        """Apply a sharpening filter using convolution"""
        # Sharpening kernel
        kernel = np.array([[0 , -1,  0],
                           [-1,  5, -1],
                           [0 , -1,  0]])

        # If grayscale image
        if img_array.ndim == 2:
            return np.clip(convolve2d(img_array, kernel, mode="same", boundary="symm"), 0, 255)

        # If RGB image → apply to each channel
        result = np.zeros_like(img_array)
        for c in range(3):
            result[:,:,c] = np.clip(convolve2d(img_array[:,:,c], kernel, mode="same", boundary="symm"), 0, 255)
        
        return result.astype(np.uint8)

    @staticmethod
    def gaussian_kernel_2D(size: int, sigma: float):
        """Generate a 2D Gaussian kernel."""

        coords = np.linspace(-(size//2) , size//2)  # also try this (for contineous intervals) 
        # coords = np.arange(-(size//2) , size//2)  # also try this (for discrete intervals) 
        xx, yy = np.meshgrid(coords, coords)
        kernel = np.exp(-(xx**2 + yy**2) / (2.0 * sigma**2))
        kernel /= kernel.sum()

        return xx, yy, kernel
    
    @staticmethod
    def gaussian_kernel_3D(size: int, sigma: float):
        """Generate a 3D Gaussian kernel."""

        return Filters.gaussian_kernel_2D(size, sigma)

    @staticmethod
    def f1(img_array):
        kernel = np.array([[-1, 0, +1],
                           [-2, 0, +2],
                           [-1, 0, +1]])
        
        # implement it by yourself

    @staticmethod
    def f2(img_array):
        kernel = np.array([[+1, +2, +1],
                           [ 0 , 0,  0],
                           [-1, -2, -1]])
        
        # implement it by yourself
