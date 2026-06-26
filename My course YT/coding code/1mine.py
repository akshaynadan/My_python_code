# #book = {"title": "To Kill a Mockingbird","author":"Harper Lee","on_shelf":False,"borrower":"Arthur Dent","overdue":True,"on_hold":False}
# #if book["overdue"] == True:# Create an if/else statement
# # Check if "book['overdue']" equals "True"
   
# #    print(book["borrower"])
#  #   print(f"Book is overdue - Contact {book["borrower"]} to return it")
   
    
# #else:
    
#     book["on_hold"] = True
#     print("Book has been put on hold")

# #borrowers_list = [
#     {
#         "name": "Alice Johnson",
#         "email": "alice.johnson@dlailibrary.com",
#         "phone": "+1111111111"
#     },
#     {
#         "name": "Bob Smith",
#         "email": "bob.smith@dlailibrary.com",
#         "phone": "+2222222222"
#     },
#     {
#         "name": "Arthur Dent",
#         "email": "arthur.dent@dlailibrary.com",
#         "phone": "+3333333333"
#     },
#     {
#         "name": "Diana Prince",
#         "email": "diana.prince@dlailibrary.com",
#         "phone": "+4444444444"
#     }
# ]
# #for names in borrowers_list:
#     if names["name"] == book["borrower"]:
#         borrower_email = names["email"]

# #print (f"{book['borrower']}'s email is: {borrower_email}")








#   def loud(text):
#         return text.upper()
# def quiet(text):
# return text.lower()
#def hello(test):
#print(text := test("Hello"))
#hello(loud)





#lists =[]
#def first(x):
#    print("Hello")
#    print(a := 10+20)
#    print(b := 20+30)
 #   def second(y):
  #      print("World")  
   #     c = y+10
    #    lists.append(c)
     #   return c
    #return second
#print(first(10)(20))
#a=first(10)
#print(a(50))
#print(lists)


text = "Hello World house"
lines = text.split(' ')
print(text)

print(lines)
if lines[0] == "Hell":
    print("good")
else:
    print("bad")
print("\n".join(lines))