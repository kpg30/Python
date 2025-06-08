'''
The isinstance() works as a comparison operator, 
it compares the object with the specified class type.
'''

input = 20
input1 = "prasad"

def check_input_type(input):
    if isinstance(input, int):
        print(f"input:{input} is Integer type")
    else:
        print(f"input:{input} is not Integer type")

check_input_type(input)

check_input_type(input1)


sample_list = ['Emma', 'Stevan', ['Jordan', 'Donald', 'Sam']]
for item in sample_list:
    if isinstance(item, list):
        print("Yes", item, 'is a nested list')



