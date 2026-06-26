#create a function called fun
#name = "walrus operator"
# create a list called food
#foods = []
#while True:
#    food = input("Enter food: ")
#    if food == "stop":
#        break
#    foods.append(food)
#print(foods)

car_list=[]
while (car := input("Enter the car name? :")) != "stop":
    car_list.append(car)
print(car_list)