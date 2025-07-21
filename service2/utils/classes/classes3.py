import logging

format = '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=format)
logger = logging.getLogger(__name__)

class TestMath:
    # def __init__(self, num, name):
    #     self.num = num
    #     self.name = name

    def findName(self, name_list):
        for name in name_list:
            if name.startswith('p'):
                print(name)

    def greet(self, name: str) -> str:
        """Display a greeting."""
        print(f"Hello {name}!")

    def cube(self, num: int) -> int:
        """Return the cube of the input number."""
        find_cube = pow(num, 3)
        return find_cube

    def findNum(self):
        for i in range(1, 10):
            if i % 3 == 0:
                continue
            print(i)

    def Loop11(self):
        while True:
            user_input = input("Type 'm' or 'M' to exit")
            if user_input.upper() == 'M':
                break


obj = TestMath()  # create an object for class

names = ['prasad', 'peter', 'james', 'bravis', 'pink']
obj.findName(names)
print("----------------------------------------")
obj.greet("Prasad")

result = obj.cube(5)

print(result)
print("----------------------------------------")
obj.findNum()
obj.Loop11()
