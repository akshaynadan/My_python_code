class Name:
    name = "hhhhh"
    print(name)
    def Say(self):
        print("Something")

def outsidefun(Name,name):
    print("Outside function")
    Name.name = name
    print(Name.name)

name_1 = Name()
outsidefun(name_1,"Rahul")

