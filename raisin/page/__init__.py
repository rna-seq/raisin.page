import os
from configobj import ConfigObj
PAGES = ConfigObj(os.path.join(os.path.dirname(__file__), "pages.ini"))
