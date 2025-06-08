import telugu as telugu

input_dict = {
    'name': "prasad",
    'age': '30',
    'gender': 'male',
    'city': 'hyderabad',
    'colors': ["red", "white", "blue"],
    'marks': {'telugu:30', 'hindi:40'}
}

get_name1 = input_dict['name']
get_name2 = input_dict.get('name')

print(input_dict)

print(get_name1)
print(get_name2)

get_marks = input_dict["marks"]
print(get_marks)

new_dict = dict(input_dict)
new_dict.pop('colors')
#new_dict.pop('marks')
del new_dict['marks']
print(f"----------after removed items from dict")
print(new_dict)


