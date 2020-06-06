# from: https://www.youtube.com/watch?v=gR73nLbbgqY
# also might be good to get data from https://www.youtube.com/watch?v=ubXXmQzzNGo
# look into click for replacing argparse?
# add tabulate to the toolbox?
# https://pypi.org/project/tabulate/


import logging

logging.basicConfig(level=logging.WARNING, format="%(msg)s")

if options.verbose:
    logging.getLogger().setLevel(logging.DEBUG)

LOG = logging.getLogger('logtest')

LOG.debug("wakka wakka")

##############################################################################

# pip install colorama

from colorama import Fore, Back, Style
colorama.init(strip=True)
print(Fore.RED + "red")
print(Back.GREEN + "back")
print(Style.BRIGHT + "bright")
print(Fore.RESET + Back.RESET + Style.RESET_ALL)


##############################################################################

# pip install progressbar2

from progressbar import *
import time

progress = ProgressBar()
for i in progress(range(80)):
    time.sleep(0.01)


