from datetime import datetime
from typing import List, Dict, Optional
import logging
#from utils.loggers.default_logger import Logger

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# logger = Logger.get_logger('classes1')
# logger = Logger.get_logger(__name__)
logger.info('######## Class example')


class ProfileInfo:

    def __init__(self, firstname: str, lastname: str, phone: Optional[str], dob: str, email: str, location: str, curr_sal: float,
                 expect_sal: float, skills: List[str], address: Dict[str, str]):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.dob = dob
        self.email = email
        self.location = location
        self.curr_sal = curr_sal
        self.expect_sal = expect_sal
        self.skills = skills
        self.address = address

    def get_fullname(self) -> str:
        fullname = self.firstname.capitalize() + " " + self.lastname.capitalize()
        return fullname

    def update_phone(self, new_phone: str) -> None:
        logger.info(f"updating phone from {self.phone} to {new_phone}")
        self.phone = new_phone

    def update_email(self, new_email: str) -> None:
        logger.info(f"updating email from {self.email} to {new_email}")
        self.email = new_email

    def get_location(self) -> str:
        return self.location.capitalize()

    def get_exp_sal(self) -> float:
        self.expect_sal = self.curr_sal * 1.30

        return self.expect_sal

    def add_skill(self, new_skill: str) -> None:
        if new_skill not in self.skills:
            self.skills.append(new_skill)
            logger.info(f"skill '{new_skill}' added.")
        else:
            logger.info(f"'{new_skill}' is already exists.")

    def has_skill(self, skill: str) -> bool:
        return skill.lower() in (s.lower() for s in self.skills)

    def compute_age(self) -> int:
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d").date()
        today = datetime.now().date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def display_profile(self) -> None:
        """ printing Profile summary """
        logger.info(f"======================= Profile Summary : {self.get_fullname()} =======================")
        logger.info(f"FullName                  :   {self.get_fullname()}")
        logger.info(f"Phone                     :   {self.phone}")
        logger.info(f"Age                       :   {self.compute_age()}")
        logger.info(f"Email                     :   {self.email}")
        logger.info(f"Current Location          :   {self.get_location()}")
        logger.info(f"Current CTC               :   {self.curr_sal}")
        logger.info(f"Expected CTC (30% Hike)   :   {self.get_exp_sal()}")
        logger.info(f"Skills                    :   {', '.join(self.skills)}")
        logger.info(f"Address                   :   {self.address}")
        logger.info("========================================================================")


def main():
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
    logger.info('\n')

    # Updating info
    profile.update_email("prasad.k@newmail.com")
    profile.update_phone("987-654-3210")
    profile.add_skill("Machine Learning")
    profile.add_skill("Python")  # Already exists

    # Check skills
    logger.info(f"Has skill 'Python'? {profile.has_skill('Python')}")
    logger.info(f"Has skill 'Java'? {profile.has_skill('Java')}")
    
    logger.info('\n')
    profile.display_profile()


if __name__ == "__main__":
    main()
