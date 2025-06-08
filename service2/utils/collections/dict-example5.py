
person = {
    "name": "Jessa", 
    "country": "USA", 
    "telephone": 1178,
    "address": "area: hyd, pincode: 500088, phone: 6476711438"
    }

class testDict:
     for key, value in person.items():
        if key == "name":
            print(f"Person name : {value}")
        else:
            print("key is not found")

def main():
    testDict()

if __name__ == "__main__":
    main()

