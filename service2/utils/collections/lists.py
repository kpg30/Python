users = ['david', 'tim', 'john']

data = ['jack', 'liu']
# index starts from 0 (zero)
print(data[0])
print(data[1])

print(users[-1])

print(users.index('tim'))

print(users[0:1])
print(users[1:])

print(len(users))

users.append('perry')
print(users)

users += ['prasad']
print(users)

users.extend(data)
users.extend(['william','smith'])
print(users)



dummy=[]

print("david" in dummy)
