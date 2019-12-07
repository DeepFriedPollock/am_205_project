import argparse
import urllib
import urllib.request
import json
import requests
import os
import re
import time
from bs4 import BeautifulSoup

url = "https://www.wikiart.org/en/paintings-by-style?sortby=2"
page = BeautifulSoup(urllib.request.urlopen(url), "lxml")

import pdb; pdb.set_trace()
