from python.service2.utils.default_logger import get_logger
import unittest
import logging

logger = get_logger('classes8')
level=logging.INFO,
format='%(asctime)s %(levelname)s %(name)s: %(message)s',
datefmt='%Y-%m-%d %H:%M:%S'
class ProcessUtils(unittest.TestCase):
    logger.info("test python code")
        
    address = {
        "city": "Hyderabad",
        "state": "Telangana",
        "country": "India"
    }

    skills = ["Python", "Data Engineer", "AWS", "Hadoop"]

    # create an object for class
    profile = ProfileInfo(
        firstname="prasad",
        lastname="k",
        phone=None,
        dob="1993-11-26",
        email="prasadk@example.com",
        location="toronto",
        curr_sal=2000,
        expect_sal=00000,
        skills=skills,
        address=address
    )
    
    profile.display_profile()
    
    