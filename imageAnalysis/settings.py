import logging
import datetime


# Flask settings
FLASK_DEBUG = True  # Do not use debug mode in production

TEMPLATES_AUTO_RELOAD = True

# Logger settings
logging.root.handlers = []

FORMAT = '%(asctime)s : %(levelname)s : %(message)s\r'

logging.basicConfig(format=FORMAT, level=logging.DEBUG,
                    filename='logs.log')

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)  # this is only if we want to error logs be printed out to console

# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s\r')
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)