import os, sys
from os.path import dirname , join ,  abspath

sys.path.insert(0, abspath(join(dirname(__file__),'..'))) # type: ignore

from payment import payment_details

def course():
    print("this is my course details")


payment_details.payment() # type: ignore