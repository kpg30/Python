person = {
    "name": "Jessa", 
    "country": "USA", 
    "telephone": 1178,
    "address": "area: hyd, pincode: 500088, phone: 6476711438"
    }

# access value using key name in []
#print(person['name'])
# get key value using key name in get()
#print(person.get('telephone'))
#get_address = person['address']
#get_address = person.get('address')
#print(get_address)
#print(get_address1)

print(person.keys())
print(person.values())
print(person.items())

for key, value in person.items():
    if key == "address":
        print(f"Person address:\n {value}")
    
    if key == "name":
        print(f"Pearson name :\n {value}")



dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
dict2 = {'Kelly': 68, 'Harry': 50, 'Emma': 66}

# # join two dictionaries with some common items
dict2.update(dict1)
dict1.update(dict2)
# # printing the updated dictionary
print(dict1)
print(dict2)

