names = ['prasad', 'bob', 'mark']


def check_length_of_string(n=['xyz', 'jkn']):
    return {name: len(name) for name in n}


def check_length_of_string1(n):
    return {name: len(name) for name in n}


def check_length_of_string3(n=None):
    if n is None:
        n = ['prasad', 'bob', 'david', 'wang']
    return {name: len(name) for name in n}


res1 = check_length_of_string()
res2 = check_length_of_string1(names)
res3 = check_length_of_string3(["hzxxkxnk", "jnw jwnkw", "nsjwnswnjwdjiowdj"])
res4 = check_length_of_string3()
print(res1)
print(res2)
print(res3)
print(res4)
