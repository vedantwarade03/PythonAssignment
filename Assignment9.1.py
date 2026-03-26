class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0
        self.address = ""

    def get_info(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = int(input("Enter salary: "))
        self.address = input("Enter address: ")

    def print_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)

class Manager(Employee):
    pass

managers = []

for i in range(10):
    print("Enter details for Manager", i+1)
    m = Manager()
    m.get_info()
    managers.append(m)

print("Information of all Managers:")
for i in range(10):
    print("\nManager", i+1)
    managers[i].print_info()