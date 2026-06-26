user =("Aksahy","nonalkshaty","robit","doctor")
passw = ["manager","12maajn","@folayte","make3445"]
date = {"look":1998,"manage":20002,"nodrad":88882222,"make":12222}
make = list(zip(user,passw,date))
formatted =[f"Name: {use} password is : {passwr} " for use ,passwr,data in make]
print(formatted)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
countries = ["USA", "UK", "Canada"]
data = list(zip(names, ages, countries))
formatted_data = [f"Name: {name}, Age: {age}, Country: {country}" for name, age, country in data]
print(formatted_data)