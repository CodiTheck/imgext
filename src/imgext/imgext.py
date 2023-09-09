#!/usr/bin/python3

""" Extract image from document.

"""

import os
import logging

import fitz
import io
from io import BytesIO
from PIL import Image


LOG = logging.getLogger(__name__)


def extract_img(file_path: str, dir_path: str) -> list:
    # STEP 2
    # file path you want to extract images from
    # file = "/content/pdf_file.pdf"

    # open the file
    pdf_file = fitz.open(file_path)
    image_files_list = []

    # STEP 3
    # iterate over PDF pages
    for page_index in range(len(pdf_file)):
        # get the page itself
        page = pdf_file[page_index]
        images_list = page.get_images()
        # print(dir(page))

        # printing number of images found in this page
        if images_list:
            LOG.info(
                f"[page {page_index:05d}] Found a total of {len(images_list)}"
            )
        else:
            LOG.info(f"[page {page_index:05d}] No images found on page.")

        for image_ind, img in enumerate(images_list, start=1):
            # get the XREF of the image
            xref = img[0]

            # extract the image bytes
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]

            # get the image extension
            image_ext = base_image["ext"]

            # save image to file:
            image_file_name = f"img{image_ind:05d}_{page_index:05d}.{image_ext}"
            image_file_path = os.path.join(dir_path, image_file_name)
            with open(image_file_path, 'wb') as imf:
                imf.write(image_bytes)

            LOG.info("  * image extension:", image_ext,
                     " - file name:", image_file_name)

            # add the image file path to the list:
            image_files_list.append(image_file_path)

    return image_files_list
