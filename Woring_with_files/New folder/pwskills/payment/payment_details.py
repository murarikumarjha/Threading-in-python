import os, sys
from os.path import dirname , join ,  abspath

sys.path.insert(0, abspath(join(dirname(__file__),'..'))) # type: ignore

from course import course_details 

def payment():
    print("this is my payment details")


course_details.course()