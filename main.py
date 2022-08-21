# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
#Import libraries
import os
from GoogleImageScrapper import GoogleImageScraper
from patch import webdriver_executable

if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    with open('SETTINGS.txt') as f:
        lines = f.readlines()
        search_keys = lines[0][14:-2].split(', ')
        number_of_images = int(lines[1][17:-1])
        FILETYPE = lines[2][9:-1]
        RESOLUTIONx, RESOLUTIONy = lines[3][11:-1].split('x')
        RESOLUTIONx, RESOLUTIONy = int(RESOLUTIONx), int(RESOLUTIONy)
        GRAYSCALE = bool(int(lines[4][10:]))

    print(search_keys)
    print("Number of images: "+str(number_of_images))
    print("Filetype: "+FILETYPE)
    print("Resolution: "+str(RESOLUTIONx)+"*"+str(RESOLUTIONy))
    print("Grayscale: "+str(GRAYSCALE))

    #Parameters
    headless = True
    min_resolution=(0,0)
    max_resolution=(9999,9999)

    #Main program
    for search_key in search_keys:
        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution, 
            FILETYPE, RESOLUTIONx, RESOLUTIONy, GRAYSCALE)
        image_urls = image_scrapper.find_image_urls()
        #image_scrapper.save_images(image_urls)
    
    #Release resources    
    del image_scrapper