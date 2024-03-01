"""Apply Image Filtering"""

#importar librerias
import numpy as np
import cv2
import sys

if __name__ == '__main__':    
# Ask the user to enter the input image name
    args = parse_user_data()   
    # Run pipeline  
    run_pipeline(args=args)