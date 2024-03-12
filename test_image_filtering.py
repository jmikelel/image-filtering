"""Test Image Filtering"""

#importar librerias
import numpy as np
import cv2
import sys
import argparse
import cvlib as cvl 


def parse_user_data():
    
        # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='Apply image '                                     
                                    'filtering')    
            # Add arguments
    parser.add_argument('-i','--input_image', 
                        type=str, 
                        required=True,
                        help='Input image to be filtered')    
    parser.add_argument('-f','--filter_name',
                        type=str,
                        required=True,
                        help="Filter name used as Kernel"
                        " [average, gaussian, median, bilateral]")
    args = parser.parse_args()

    # Return parsed data entered by the user
    return args


def run_pipeline(args:argparse.Namespace)->None:
     
     # Load image
     img = cvl.load_image(args.input_image)
     print(f"Image size: {img.shape}")
         



if __name__ == '__main__':    
    # Ask the user to enter the input image name
    args = parse_user_data()

    # Run pipeline    
    run_pipeline(args=args)