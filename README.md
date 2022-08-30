Adapted code from Oh Yicong: https://github.com/ohyicong/Google-Image-Scraper

For detailed installation please refer to Yicong's Github

# Main Changes
1. Added a scaling parameter for downloaded images
2. Added a grayscale converstion option for downloaded images
3. Added a file type option (e.g. png/jpg) when saving images
4. Improved performance of scrapper (scrapping speed and user friendliness)
5. Fixed minor bugs and issues (such as not downloading specified number of images)

# Usage
Run main.py to scrape google images.
Change settings file to edit parameters.

Example:

SEARCH_TERMS=[cat, dog]  

NUMBER_OF_IMAGES=5  

RESOLUTION=300x300 (0x0 to save in native resolution)

GRAYSCALE=False  

FILETYPE = JPEG/PNG

## Pre-requisites:
1. Pip install Selenium Library
2. Pip install PIL
3. Download Google Chrome 
4. Download Google Webdriver based on your Chrome version (To check Chrome version: more options --> Help --> About Google Chrome)
