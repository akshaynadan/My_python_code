# create a color with differnt items in a dress store
import functools

number =[2,3,4,5,6,7,8,9,10]
number.sort(reverse=True)
print(number)

print(functools.reduce(lambda x,y:x**y,number))




