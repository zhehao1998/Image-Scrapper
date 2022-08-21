Adapted code from Oh Yicong: https://github.com/ohyicong/Google-Image-Scraper

For detailed installation please refer to Yicong's Github

# Main Changes
1. Added a scaling parameter for downloaded images
2. Added a grayscale option when downloading
3. Added a file type option (e.g. png/jpg) when saving images
4. Improved scrapping speed of scrapper
5. Fixed minor bugs and ensure web scrapper downloaded exactly the number of items requested

# Usage
Run main.py to scrape google images.
Change settings file to edit parameters.

Example:

SEARCH_TERMS=[loackers, quadratini]
NUMBER_OF_IMAGES=5
FILETYPE=PNG
RESOLUTION=300x300
GRAYSCALE=False

FILETYPE = JPEG/PNG
RESOLUTION = 0x0 to save in default resolution.

## Pre-requisites:
1. Pip install Selenium Library
2. Pip install PIL
3. Download Google Chrome 
4. Download Google Webdriver based on your Chrome version
