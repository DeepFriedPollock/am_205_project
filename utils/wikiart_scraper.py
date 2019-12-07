import argparse
import urllib
import urllib.request
import json
import requests
import os
import re
import time


style_list = ['impressionism', 'realism', 'romanticism', 'expressionism',
             'post-impressionism', 'surrealism', 'art-nouveau', 'baroque',
             'symbolism', 'abstract-expressionism', 'na-ve-art-primitivism',
             'neoclassicism', 'cubism', 'rococo', 'northern-renaissance',
             'pop-art', 'minimalism', 'abstract-art', 'art-informel', 'ukiyo-e',
             'conceptual-art', 'color-field-painting', 'high-renaissance',
             'mannerism-late-renaissance', 'neo-expressionism', 'early-renaissance',
             'magic-realism', 'academicism', 'op-art', 'lyrical-abstraction',
             'contemporary-realism', 'art-deco', 'fauvism', 'concretism',
             'ink-and-wash-painting', 'post-minimalism', 'social-realism',
             'hard-edge-painting', 'neo-romanticism', 'tachisme', 'pointillism',
             'socialist-realism', 'neo-pop-art']


FOLDER_NAME = "scraped_images"
STYLE_TO_SCRAPE = 'neo-expressionism'


import pdb; pdb.set_trace()
import sys; sys.exit()


def setup_scrape_folder(path):
    if not os.path.isdir(path):
        print("Creating scraped_images directory to store files")
        try:
            os.mkdir(path)
        except OSError:
            print("Did not create scraped_images directory; you've already made it" % path)
        else:
            print("Successfully created the directory %s" % path)

TOTAL_PAGES = 65

def main():
    pass
    # total_paintings_saved = 0
    # setup_scrape_folder(f"./{FOLDER_NAME}")
    # for page in range(1, TOTAL_PAGES):
    #
    #     url = f"https://www.wikiart.org/en/paintings-by-style/{STYLE_TO_SCRAPE}?select=featured&json=2&layout=new&page={page}&resultType=masonry"
    #     request_response = requests.get(url)
    #     try:
    #         all_paintings = json.loads(request_response.content.decode("utf-8"))['Paintings']
    #     except:
    #         print(f"Unable to grab paintings for page {page}. Either the scraping has completed or there was an error")
    #         sys.exit()
    #     for painting in all_paintings:
    #         # Sleep just in case, so we don't overwhelm the server
    #         time.sleep(0.01)
    #         # make sure sub-folder for style is set up
    #         setup_scrape_folder(f"./{FOLDER_NAME}/{STYLE_TO_SCRAPE}")
    #         image_url = painting['image']
    #         # Make file name to save images to
    #         image_name = re.search("/images/(.*)", image_url).groups()[0]
    #         image_name = image_name.replace("/", "_")
    #
    #         file_name = f"{FOLDER_NAME}/{STYLE_TO_SCRAPE}/{image_name}"
    #         try:
    #             image = urllib.request.urlretrieve(image_url, file_name)
    #             total_paintings_saved += 1
    #             print(f"Saved image: {file_name}. Total images saved so far: {total_paintings_saved}")
    #         except:
    #             print(f"Unable to save {image_url}")


if __name__ == '__main__':
    main()
