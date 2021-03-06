"""
OCT image SRF detection wrapper. (Calling the main .py file of this program 'oct_srf_detection.py')

Classification of OCT images for the retinal disease bio-marker SRF (sub-retinal fluid).
This is the file to run for completing the task and output the classification of the
given images and some summary statistics.

final exercise from the lecture:
Introduction to Signal and Image Processing FS19
by:
Prof. Raphael Sznitman

See README.md for the full exercise description.
"""

__author__ = "Jan Wälchli, Mario Moser, Dominik Meise"
__copyright__ = "Copyright 2019; Jan Wälchli, Mario Moser, Dominik Meise; All rigths reserved."
__email__ = "dominik.meise@students.unibe.ch"


import sys
import oct_srf_detection


if __name__ == '__main__':
    sys.stdout = oct_srf_detection.Logger()
    oct_srf_detection.main()
